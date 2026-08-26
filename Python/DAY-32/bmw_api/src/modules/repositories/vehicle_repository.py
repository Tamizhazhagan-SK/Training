from abc import ABC, abstractmethod
from typing import List

from modules.dtos.vehicle_request import VehicleRequest
from modules.models.vehicle import Vehicle


class VehicleRepository(ABC):
    @abstractmethod
    async def get_vehicle_by_id(self, vehicle_id: int) -> Vehicle:
        pass

    @abstractmethod
    async def get_all_vehicles(self) -> List[Vehicle]:
        pass

    @abstractmethod
    async def create_vehicle(self, vehicle_data: VehicleRequest) -> Vehicle:
        pass

    @abstractmethod
    async def update_vehicle(self, vehicle_id: int, vehicle_data: VehicleRequest) -> Vehicle:
        pass

    @abstractmethod
    async def delete_vehicle(self, vehicle_id: int) -> bool:
        pass