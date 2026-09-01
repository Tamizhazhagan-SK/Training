from datetime import date
from pydantic import BaseModel, Field
from models.appointment import AppointmentStatus


class AppointmentCreateRequest(BaseModel):
    vin: str = Field(..., min_length=5, max_length=20)
    customer_name: str = Field(..., min_length=2, max_length=100)
    service_type: str = Field(..., min_length=2, max_length=50)
    service_date: date
    service_center: str = Field(..., min_length=2, max_length=50)
    status: AppointmentStatus = AppointmentStatus.SCHEDULED

    class Config:
        json_schema_extra = {
            "example": {
                "vin": "BMWX3001",
                "customer_name": "Arun Kumar",
                "service_type": "Periodic Service",
                "service_date": "2026-09-10",
                "service_center": "BMW Chennai",
                "status": "SCHEDULED",
            }
        }


class AppointmentUpdateRequest(BaseModel):
    vin: str = Field(..., min_length=5, max_length=20)
    customer_name: str = Field(..., min_length=2, max_length=100)
    service_type: str = Field(..., min_length=2, max_length=50)
    service_date: date
    service_center: str = Field(..., min_length=2, max_length=50)
    status: AppointmentStatus
