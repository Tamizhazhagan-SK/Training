from pydantic import BaseModel, Field
from models.vehicle import FuelType


class VehicleCreateRequest(BaseModel):
    vin: str = Field(..., min_length=5, max_length=20, description="Vehicle Identification Number")
    model: str = Field(..., min_length=2, max_length=50)
    year: int = Field(..., ge=1990, le=2100)
    fuel_type: FuelType
    color: str = Field(..., min_length=2, max_length=30)
    price: float = Field(..., gt=0)

    class Config:
        json_schema_extra = {
            "example": {
                "vin": "BMWX5VIN001",
                "model": "BMW X5",
                "year": 2026,
                "fuel_type": "Petrol",
                "color": "Black",
                "price": 9500000,
            }
        }


class VehicleUpdateRequest(BaseModel):
    vin: str = Field(..., min_length=5, max_length=20)
    model: str = Field(..., min_length=2, max_length=50)
    year: int = Field(..., ge=1990, le=2100)
    fuel_type: FuelType
    color: str = Field(..., min_length=2, max_length=30)
    price: float = Field(..., gt=0)
