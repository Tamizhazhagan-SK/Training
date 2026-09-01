from pydantic import BaseModel, Field
from models.vehicle import VehicleStatus


class VehicleCreateRequest(BaseModel):
    vin: str = Field(..., min_length=5, max_length=30)
    model: str = Field(..., min_length=2, max_length=50)
    price: float = Field(..., gt=0)
    dealer_id: int = Field(..., gt=0)
    status: VehicleStatus = VehicleStatus.AVAILABLE

    class Config:
        json_schema_extra = {
            "example": {
                "vin": "BMWIX001",
                "model": "BMW iX",
                "price": 12500000,
                "dealer_id": 101,
                "status": "AVAILABLE",
            }
        }


class VehicleResponse(BaseModel):
    vehicle_id: int
    vin: str
    model: str
    price: float
    dealer_id: int
    status: VehicleStatus

    class Config:
        from_attributes = True
