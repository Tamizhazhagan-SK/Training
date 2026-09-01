from enum import Enum
from pydantic import BaseModel, Field


class FuelType(str, Enum):
    PETROL = "Petrol"
    DIESEL = "Diesel"
    ELECTRIC = "Electric"
    HYBRID = "Hybrid"


class Vehicle(BaseModel):
    """Internal representation of a vehicle stored in the system."""
    id: int
    vin: str
    model: str
    year: int
    fuel_type: FuelType
    color: str
    price: float
