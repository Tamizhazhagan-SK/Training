from typing import List

from sqlalchemy import select

from modules.configurations.psql_connection import PGConnection
from modules.dtos.vehicle_request import VehicleRequest
from modules.exceptions.vehicle_not_found_exception import VehicleNotFoundException
from modules.exceptions.vehicledata_exception import VehicleDataException
from modules.models.vehicle import Vehicle
from modules.repositories.vehicle_repository import VehicleRepository


class VehicleRepositoryImpl(VehicleRepository):

    def __init__(self):
        self.session = PGConnection.get_session()

    async def get_vehicle_by_id(self, vehicle_id: int) -> Vehicle:
        result = await self.session.execute(select(Vehicle).where(Vehicle.id == vehicle_id))
        vehicle = result.scalar_one_or_none()
        if not vehicle:
            raise VehicleNotFoundException(f"Vehicle with ID {vehicle_id} not found.")
        return vehicle

    async def get_all_vehicles(self) -> List[Vehicle]:
        result = await self.session.execute(select(Vehicle))
        return list(result.scalars().all())

    async def create_vehicle(self, vehicle_data: VehicleRequest) -> Vehicle:
        new_vehicle = Vehicle(
            make=vehicle_data.make,
            model=vehicle_data.model,
            year=vehicle_data.year,
            vin=vehicle_data.vin,
        )
        try:
            self.session.add(new_vehicle)
            await self.session.commit()
            await self.session.refresh(new_vehicle)
            return new_vehicle
        except Exception:
            await self.session.rollback()
            raise VehicleDataException("Error occurred while creating the vehicle.")

    async def update_vehicle(self, vehicle_id: int, vehicle_data: VehicleRequest) -> Vehicle:
        result = await self.session.execute(select(Vehicle).where(Vehicle.id == vehicle_id))
        vehicle = result.scalar_one_or_none()
        if not vehicle:
            raise VehicleNotFoundException(f"Vehicle with ID {vehicle_id} not found.")

        try:
            vehicle.make = vehicle_data.make
            vehicle.model = vehicle_data.model
            vehicle.year = vehicle_data.year
            vehicle.vin = vehicle_data.vin
            await self.session.commit()
            await self.session.refresh(vehicle)
            return vehicle
        except Exception:
            await self.session.rollback()
            raise VehicleDataException(f"Error occurred while updating the vehicle with ID {vehicle_id}.")

    async def delete_vehicle(self, vehicle_id: int) -> bool:
        result = await self.session.execute(select(Vehicle).where(Vehicle.id == vehicle_id))
        vehicle = result.scalar_one_or_none()
        if not vehicle:
            raise VehicleNotFoundException(f"Vehicle with ID {vehicle_id} not found.")

        try:
            await self.session.delete(vehicle)
            await self.session.commit()
            return True
        except Exception:
            await self.session.rollback()
            raise VehicleDataException(f"Error occurred while deleting the vehicle with ID {vehicle_id}.")
