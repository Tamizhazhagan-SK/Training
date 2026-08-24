from typing import List

from modules.configurations.psql_connection import PGConnection
from modules.dtos.vehicle_request import VehicleRequest
from modules.exceptions.vehicle_not_found_exception import VehicleNotFoundException
from modules.exceptions.vehicledata_exception import VehicleDataException
from modules.models.vehicle import Vehicle
from modules.repositories.vehicle_repository import VehicleRepository


class VehicleRepositoryImplementation(VehicleRepository):

    def __init__(self):
        self.session = PGConnection.get_session()

    def get_vehicle_by_id(self, vehicle_id: int) -> Vehicle:
        vehicle = self.session.query(Vehicle).filter_by(id=vehicle_id).first()
        if not vehicle:
            raise VehicleNotFoundException(f"Vehicle with ID {vehicle_id} not found.")
        return vehicle

    def get_all_vehicles(self) -> List[Vehicle]:
        return self.session.query(Vehicle).all()

    def create_vehicle(self, vehicle_data: VehicleRequest) -> Vehicle:
        new_vehicle = Vehicle(
            make=vehicle_data.make,
            model=vehicle_data.model,
            year=vehicle_data.year,
            vin=vehicle_data.vin,
        )
        try:
            self.session.add(new_vehicle)
            self.session.commit()
            return new_vehicle
        except Exception:
            self.session.rollback()
            raise VehicleDataException("Error occurred while creating the vehicle.")

    def update_vehicle(self, vehicle_id: int, vehicle_data: VehicleRequest) -> Vehicle:
        vehicle = self.session.query(Vehicle).filter_by(id=vehicle_id).first()
        if not vehicle:
            raise VehicleNotFoundException(f"Vehicle with ID {vehicle_id} not found.")

        try:
            vehicle.make = vehicle_data.make
            vehicle.model = vehicle_data.model
            vehicle.year = vehicle_data.year
            vehicle.vin = vehicle_data.vin
            self.session.commit()
            return vehicle
        except Exception:
            self.session.rollback()
            raise VehicleDataException(f"Error occurred while updating the vehicle with ID {vehicle_id}.")

    def delete_vehicle(self, vehicle_id: int) -> bool:
        vehicle = self.session.query(Vehicle).filter_by(id=vehicle_id).first()
        if not vehicle:
            raise VehicleNotFoundException(f"Vehicle with ID {vehicle_id} not found.")

        try:
            self.session.delete(vehicle)
            self.session.commit()
            return True
        except Exception:
            self.session.rollback()
            raise VehicleDataException(f"Error occurred while deleting the vehicle with ID {vehicle_id}.")
