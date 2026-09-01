from datetime import datetime
from typing import List
from pydantic import BaseModel

from models.health import AlertType, EngineStatus, BatteryStatus, FuelStatus, OverallStatus


class TelemetryResponse(BaseModel):
    reading_id: int
    vehicle_id: str
    speed: float
    engine_temperature: float
    battery_level: float
    fuel_level: float
    latitude: float
    longitude: float
    recorded_at: datetime

    class Config:
        from_attributes = True


class AlertResponse(BaseModel):
    vehicle_id: str
    alert: AlertType


class TelemetryIngestResponse(BaseModel):
    """Returned when a telemetry reading is submitted; includes any alerts it triggered."""
    reading: TelemetryResponse
    alerts: List[AlertResponse]


class VehicleHealthResponse(BaseModel):
    vehicle_id: str
    engine_status: EngineStatus
    battery_status: BatteryStatus
    fuel_status: FuelStatus
    overall_status: OverallStatus
