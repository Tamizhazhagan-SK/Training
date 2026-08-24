from enum import Enum

class FuelType(Enum):
    """An enumeration representing various fuel types available for vehicles.

    Attributes:
        PETROL (str): Petrol/Gasoline fuel type.
        DIESEL (str): Diesel fuel type.
        GAS (str): Compressed natural gas or LPG fuel type.
    """
    
    PETROL = "Petrol"
    DIESEL = "Diesel"
    GAS = "Gas"