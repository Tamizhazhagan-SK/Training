from pydantic import BaseModel
from models.vehicle import FuelType


class VehicleResponse(BaseModel):
    id: int
    vin: str
    model: str
    year: int
    fuel_type: FuelType
    color: str
    price: float

    class Config:
        from_attributes = True
