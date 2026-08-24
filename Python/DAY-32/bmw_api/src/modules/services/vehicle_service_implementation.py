from typing import List

from modules.dtos.vehicle_request import VehicleRequest
from modules.dtos.vehicle_response import VehicleResponse
from modules.repositories.vehicle_repository_implementation import VehicleRepositoryImpl
from modules.services.vehicle_service import VehicleService


class VehicleServiceImpl(VehicleService):
    def __init__(self):
        self.vehicle_repository = VehicleRepositoryImpl()

    def get_all_vehicles(self) -> List[VehicleResponse]:
        vehicles = self.vehicle_repository.get_all_vehicles()
        return [
            VehicleResponse(
                id=vehicle.id,
                make=vehicle.make,
                model=vehicle.model,
                year=vehicle.year,
                vin=vehicle.vin,
                created_at=vehicle.created_at,
                updated_at=vehicle.updated_at,
            )
            for vehicle in vehicles
        ]

    def get_vehicle_by_id(self, vehicle_id: int) -> VehicleResponse:
        vehicle = self.vehicle_repository.get_vehicle_by_id(vehicle_id)
        return VehicleResponse(
            id=vehicle.id,
            make=vehicle.make,
            model=vehicle.model,
            year=vehicle.year,
            vin=vehicle.vin,
            created_at=vehicle.created_at,
            updated_at=vehicle.updated_at,
        )

    def create_vehicle(self, vehicle_request: VehicleRequest) -> VehicleResponse:
        vehicle = self.vehicle_repository.create_vehicle(vehicle_request)
        return VehicleResponse(
            id=vehicle.id,
            make=vehicle.make,
            model=vehicle.model,
            year=vehicle.year,
            vin=vehicle.vin,
            created_at=vehicle.created_at,
            updated_at=vehicle.updated_at,
        )

    def update_vehicle(self, vehicle_id: int, vehicle_data: VehicleRequest) -> VehicleResponse:
        vehicle = self.vehicle_repository.update_vehicle(vehicle_id, vehicle_data)
        return VehicleResponse(
            id=vehicle.id,
            make=vehicle.make,
            model=vehicle.model,
            year=vehicle.year,
            vin=vehicle.vin,
            created_at=vehicle.created_at,
            updated_at=vehicle.updated_at,
        )

    def delete_vehicle(self, vehicle_id: int) -> bool:
        return self.vehicle_repository.delete_vehicle(vehicle_id)