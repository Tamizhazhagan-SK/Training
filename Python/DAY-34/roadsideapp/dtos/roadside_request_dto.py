from pydantic import BaseModel, Field
from models.status import RequestStatus


class RoadsideRequestCreate(BaseModel):
    vehicle_id: str = Field(..., min_length=2, max_length=20)
    vin: str = Field(..., min_length=5, max_length=30)
    issue: str = Field(..., min_length=2, max_length=200)
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)

    class Config:
        json_schema_extra = {
            "example": {
                "vehicle_id": "BMW001",
                "vin": "BMWVIN00981",
                "issue": "Flat tyre",
                "latitude": 13.0827,
                "longitude": 80.2707,
            }
        }


class AssignTechnicianRequest(BaseModel):
    technician_id: str = Field(..., min_length=1, max_length=20)
    technician_name: str = Field(..., min_length=2, max_length=100)

    class Config:
        json_schema_extra = {
            "example": {"technician_id": "TECH42", "technician_name": "Karthik S"}
        }


class StatusUpdateRequest(BaseModel):
    status: RequestStatus

    class Config:
        json_schema_extra = {"example": {"status": "IN_PROGRESS"}}
