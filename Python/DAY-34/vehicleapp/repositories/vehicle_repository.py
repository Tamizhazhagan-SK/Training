from typing import Dict, List, Optional
from models.vehicle import Vehicle


class VehicleRepository:
    """Simple in-memory 'database' for vehicles.

    Swap this out for a SQLAlchemy-backed repository later without
    touching the service or controller layers.
    """

    def __init__(self) -> None:
        self._vehicles: Dict[int, Vehicle] = {}
        self._next_id: int = 1

    def create(self, vehicle_data: dict) -> Vehicle:
        vehicle = Vehicle(id=self._next_id, **vehicle_data)
        self._vehicles[self._next_id] = vehicle
        self._next_id += 1
        return vehicle

    def get_all(self) -> List[Vehicle]:
        return list(self._vehicles.values())

    def get_by_id(self, vehicle_id: int) -> Optional[Vehicle]:
        return self._vehicles.get(vehicle_id)

    def update(self, vehicle_id: int, vehicle_data: dict) -> Optional[Vehicle]:
        if vehicle_id not in self._vehicles:
            return None
        updated_vehicle = Vehicle(id=vehicle_id, **vehicle_data)
        self._vehicles[vehicle_id] = updated_vehicle
        return updated_vehicle

    def delete(self, vehicle_id: int) -> bool:
        if vehicle_id not in self._vehicles:
            return False
        del self._vehicles[vehicle_id]
        return True

    def exists_by_vin(self, vin: str, exclude_id: Optional[int] = None) -> bool:
        return any(
            v.vin == vin for vid, v in self._vehicles.items() if vid != exclude_id
        )
