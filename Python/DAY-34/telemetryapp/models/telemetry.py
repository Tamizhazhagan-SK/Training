from datetime import datetime
from pydantic import BaseModel


class TelemetryReading(BaseModel):
    """A single sensor reading received from a connected vehicle."""
    reading_id: int
    vehicle_id: str
    speed: float
    engine_temperature: float
    battery_level: float
    fuel_level: float
    latitude: float
    longitude: float
    recorded_at: datetime
