from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from models.status import RequestStatus


class RoadsideRequestResponse(BaseModel):
    request_id: int
    vehicle_id: str
    vin: str
    issue: str
    latitude: float
    longitude: float
    status: RequestStatus
    estimated_arrival_minutes: int
    technician_id: Optional[str] = None
    technician_name: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
