from typing import List, Optional
from fastapi import HTTPException, status

from repositories.vehicle_repository import VehicleRepository
from repositories.dealer_repository import DealerRepository
from dtos.vehicle_dto import VehicleCreateRequest
from models.vehicle import Vehicle


class VehicleService:
    def __init__(
        self,
        vehicle_repository: VehicleRepository,
        dealer_repository: DealerRepository,
    ) -> None:
        self._vehicle_repository = vehicle_repository
        self._dealer_repository = dealer_repository

    def create_vehicle(self, request: VehicleCreateRequest) -> Vehicle:
        if self._dealer_repository.get_by_id(request.dealer_id) is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Dealer with id {request.dealer_id} not found",
            )
        if self._vehicle_repository.exists_by_vin(request.vin):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Vehicle with VIN '{request.vin}' already exists",
            )
        return self._vehicle_repository.create(request.model_dump())

    def get_all_vehicles(
        self,
        model: Optional[str] = None,
        city: Optional[str] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
    ) -> List[Vehicle]:
        return self._vehicle_repository.get_all(
            model=model, city=city, min_price=min_price, max_price=max_price
        )

    def get_vehicle(self, vehicle_id: int) -> Vehicle:
        vehicle = self._vehicle_repository.get_by_id(vehicle_id)
        if vehicle is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Vehicle with id {vehicle_id} not found",
            )
        return vehicle

    def get_vehicles_for_dealer(self, dealer_id: int) -> List[Vehicle]:
        # Ensures 404 is raised if the dealer doesn't exist
        if self._dealer_repository.get_by_id(dealer_id) is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Dealer with id {dealer_id} not found",
            )
        return self._vehicle_repository.get_by_dealer(dealer_id)

    def mark_sold(self, vehicle_id: int) -> Vehicle:
        # Ensures 404 is raised if the vehicle doesn't exist
        self.get_vehicle(vehicle_id)

        try:
            updated = self._vehicle_repository.mark_sold(vehicle_id)
        except ValueError as exc:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=str(exc),
            ) from exc

        return updated
