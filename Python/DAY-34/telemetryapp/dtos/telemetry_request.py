from pydantic import BaseModel, Field


class TelemetryCreateRequest(BaseModel):
    vehicle_id: str = Field(..., min_length=2, max_length=20)
    speed: float = Field(..., ge=0, le=400)
    engine_temperature: float = Field(..., ge=-50, le=300)
    battery_level: float = Field(..., ge=0, le=100)
    fuel_level: float = Field(..., ge=0, le=100)
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)

    class Config:
        json_schema_extra = {
            "example": {
                "vehicle_id": "BMW001",
                "speed": 92,
                "engine_temperature": 98,
                "battery_level": 72,
                "fuel_level": 35,
                "latitude": 13.0827,
                "longitude": 80.2707,
            }
        }
