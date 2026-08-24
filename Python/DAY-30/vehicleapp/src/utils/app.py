"""Vehicle Factory Module.

This module provides factory functions to instantiate different types of 
vehicles (Standard, Electric, and Hybrid) based on input data dictionaries.
"""

from models.vehicle import Vehicle
from models.hybrid_vehicle import HybridVehicle
from models.e_vehicle import ElectricVehicle
from models.fuel_type import FuelType
from models.e_system import ElectricSystem
from models.adas_system import ADAS
from models.variant import Variant
from utils.nav_app import create_navigation

def create_vehicle(vehicle_data): 
    """Create and return a vehicle instance based on the provided data dictionary.

    Parameters:
        vehicle_data (dict): A dictionary containing vehicle details such as 
            `vin`, `model`, and optionally `battery_kwh` and `fuel_type`.

    Returns:
        Vehicle: An instance of `Vehicle`, `ElectricVehicle`, or `HybridVehicle` 
        depending on the supplied parameters.

    Example:
        >>> data = {"vin": "123", "model": "Tesla", "battery_kwh": 75}
        >>> create_vehicle(data)
        <ElectricVehicle: Tesla>
    """
    adas_system = None
    if "adas" in vehicle_data:
        adas_system = ADAS(
            name=vehicle_data["adas"]["name"],
        )

    navigation_system = None
    if "variant" in vehicle_data and "navigation" in vehicle_data:
        navigation_system = create_navigation(
            variant=vehicle_data["variant"],
            navigation_data=vehicle_data["navigation"]
        )

    if "battery_kwh" in vehicle_data and vehicle_data.get("fuel_type") is not None:
        vehicle = HybridVehicle(
            vin=vehicle_data["vin"],
            model=vehicle_data["model"],
            battery_kwh=vehicle_data["battery_kwh"],
            fuel_type=vehicle_data["fuel_type"],
            adas=adas_system,
            navigation=navigation_system
        )
    elif "battery_kwh" in vehicle_data:
        vehicle = ElectricVehicle(
            vin=vehicle_data["vin"],
            model=vehicle_data["model"],
            battery_kwh=vehicle_data["battery_kwh"],
            voltage=vehicle_data["voltage"],
            capacity=vehicle_data["capacity"],
            adas=adas_system,
            navigation=navigation_system
        )
    elif "voltage" in vehicle_data and "capacity" in vehicle_data:
        vehicle = ElectricSystem(
            vin=vehicle_data["vin"],
            model=vehicle_data["model"],
            navigation=navigation_system
        )

    elif adas_system is not None:
        vehicle = Vehicle(
            vin=vehicle_data["vin"],
            model=vehicle_data["model"],
            adas=adas_system,
            navigation=navigation_system
        )    
    else:
        vehicle = Vehicle(
            vin=vehicle_data["vin"],
            model=vehicle_data["model"],
            navigation=navigation_system
        )
    return vehicle  


if __name__ == "__main__":

    # instance = create_vehicle(vehicle_data = {
    #     "vin": "1HGCM82633A123456",
    #     "model": "Honda Accord"
    #     # "battery_kwh": -75 
    # })

    # instance2 = create_vehicle(vehicle_data = {
    #     "vin": "1HGCM82633A654321",
    #     "model": "Toyota Camry",
    #     "battery_kwh": 50,
    #     "fuel_type": FuelType.PETROL
    # })

    # instance3 = create_vehicle(vehicle_data = {
    #     "vin": "1HGCM82633A987654",
    #     "model": "Ford Fusion",
    #     "battery_kwh": 60
    # })

    instance4 = create_vehicle(vehicle_data = {
        "vin": "1HGCM82633A111111",
        "model": "Chevrolet Volt",
        "battery_kwh": 40,
        "voltage": 400,
        "capacity": 60,
        "adas": {
            "name": "Advanced Driver Assistance System",
        }
    })

    #call power method for the newly added power method in Vehicle class
    instance4.power()

    # print(instance)
    # print(repr(instance))

    # print(instance2)
    # print(repr(instance2))

    # print(instance3)
    # print(repr(instance3))

    print(instance4.power())
    adas_details = instance4.get_adas()
    print(adas_details)
    print(adas_details["adas"].activate_adas())