from typing import List
from fastapi import HTTPException, status

from repositories.vehicle_repository import VehicleRepository
from dtos.vehicle_request import VehicleCreateRequest, VehicleUpdateRequest
from models.vehicle import Vehicle


class VehicleService:
    def __init__(self, repository: VehicleRepository) -> None:
        self._repository = repository

    def create_vehicle(self, request: VehicleCreateRequest) -> Vehicle:
        if self._repository.exists_by_vin(request.vin):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Vehicle with VIN '{request.vin}' already exists",
            )
        return self._repository.create(request.model_dump())

    def get_all_vehicles(self) -> List[Vehicle]:
        return self._repository.get_all()

    def get_vehicle(self, vehicle_id: int) -> Vehicle:
        vehicle = self._repository.get_by_id(vehicle_id)
        if vehicle is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Vehicle with id {vehicle_id} not found",
            )
        return vehicle

    def update_vehicle(self, vehicle_id: int, request: VehicleUpdateRequest) -> Vehicle:
        # Ensures 404 is raised if it doesn't exist
        self.get_vehicle(vehicle_id)

        if self._repository.exists_by_vin(request.vin, exclude_id=vehicle_id):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Another vehicle already uses VIN '{request.vin}'",
            )

        updated = self._repository.update(vehicle_id, request.model_dump())
        return updated

    def delete_vehicle(self, vehicle_id: int) -> None:
        # Ensures 404 is raised if it doesn't exist
        self.get_vehicle(vehicle_id)
        self._repository.delete(vehicle_id)
