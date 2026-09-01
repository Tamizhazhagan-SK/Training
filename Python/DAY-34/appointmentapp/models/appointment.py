from datetime import date
from enum import Enum
from pydantic import BaseModel


class AppointmentStatus(str, Enum):
    SCHEDULED = "SCHEDULED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class Appointment(BaseModel):
    """Internal representation of a service appointment."""
    appointment_id: int
    vin: str
    customer_name: str
    service_type: str
    service_date: date
    service_center: str
    status: AppointmentStatus
