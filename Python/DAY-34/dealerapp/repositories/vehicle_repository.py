from typing import List, Optional
from sqlalchemy.orm import Session

from models.vehicle import Vehicle, VehicleStatus
from models.dealer import Dealer


class VehicleRepository:
    def __init__(self, db: Session) -> None:
        self._db = db

    def create(self, data: dict) -> Vehicle:
        vehicle = Vehicle(**data)
        self._db.add(vehicle)
        self._db.commit()
        self._db.refresh(vehicle)
        return vehicle

    def get_all(
        self,
        model: Optional[str] = None,
        city: Optional[str] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
    ) -> List[Vehicle]:
        query = self._db.query(Vehicle)

        if city is not None:
            # city lives on the related Dealer, so join to filter by it
            query = query.join(Dealer, Vehicle.dealer_id == Dealer.dealer_id).filter(
                Dealer.city == city
            )
        if model is not None:
            query = query.filter(Vehicle.model == model)
        if min_price is not None:
            query = query.filter(Vehicle.price >= min_price)
        if max_price is not None:
            query = query.filter(Vehicle.price <= max_price)

        return query.all()

    def get_by_id(self, vehicle_id: int) -> Optional[Vehicle]:
        return self._db.query(Vehicle).filter(Vehicle.vehicle_id == vehicle_id).first()

    def get_by_dealer(self, dealer_id: int) -> List[Vehicle]:
        return self._db.query(Vehicle).filter(Vehicle.dealer_id == dealer_id).all()

    def exists_by_vin(self, vin: str) -> bool:
        return self._db.query(Vehicle).filter(Vehicle.vin == vin).first() is not None

    def mark_sold(self, vehicle_id: int) -> Optional[Vehicle]:
        """Transactionally flip a vehicle from AVAILABLE to SOLD.

        Returns the updated vehicle, or None if it doesn't exist.
        Raises ValueError if it isn't currently AVAILABLE.
        """
        vehicle = self.get_by_id(vehicle_id)
        if vehicle is None:
            return None
        if vehicle.status != VehicleStatus.AVAILABLE:
            raise ValueError(
                f"Vehicle {vehicle_id} is not AVAILABLE (current status: {vehicle.status.value})"
            )

        try:
            vehicle.status = VehicleStatus.SOLD
            self._db.commit()
            self._db.refresh(vehicle)
            return vehicle
        except Exception:
            self._db.rollback()
            raise
