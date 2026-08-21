from models.vehicle import Vehicle
from models.hybrid_vehicle import HybridVehicle
from models.e_vehicle import ElectricVehicle
from models.fuel_type import FuelType

def create_vehicle(vehicle_data):    
    if "battery_kwh" in vehicle_data and "fuel_type" in vehicle_data:
        vehicle = HybridVehicle(
            vin=vehicle_data["vin"],
            model=vehicle_data["model"],
            battery_kwh=vehicle_data["battery_kwh"],
            fuel_type=vehicle_data["fuel_type"]
        )

    if "battery_kwh" in vehicle_data and "fuel_type" == None:
        vehicle = ElectricVehicle(
            vin=vehicle_data["vin"],
            model=vehicle_data["model"],
            battery_kwh=vehicle_data["battery_kwh"]
        )

    else:
        vehicle = Vehicle(
            vin=vehicle_data["vin"],
            model=vehicle_data["model"]
        )
    return vehicle  


if __name__ == "__main__":

    instance= create_vehicle(vehicle_data = {
        "vin": "1HGCM82633A123456",
        "model": "Honda Accord"
        # "battery_kwh": -75 
    })

    instance2= create_vehicle(vehicle_data = {
        "vin": "1HGCM82633A654321",
        "model": "Toyota Camry",
        "battery_kwh": 50,
        "fuel_type": FuelType.PETROL
    })

    instance3= create_vehicle(vehicle_data = {
        "vin": "1HGCM82633A987654",
        "model": "Ford Fusion",
        "battery_kwh": 60
    })

    print(instance)
    print(repr(instance))

    print(instance2)
    print(repr(instance2))

    print(instance3)
    print(repr(instance3))


