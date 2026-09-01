from datetime import date
from pydantic import BaseModel
from models.appointment import AppointmentStatus


class AppointmentResponse(BaseModel):
    appointment_id: int
    vin: str
    customer_name: str
    service_type: str
    service_date: date
    service_center: str
    status: AppointmentStatus

    class Config:
        from_attributes = True
