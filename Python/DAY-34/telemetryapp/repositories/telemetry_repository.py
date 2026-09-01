from datetime import datetime
from typing import Dict, List, Optional
from models.telemetry import TelemetryReading


class TelemetryRepository:
    """In-memory store of telemetry readings, grouped by vehicle_id.

    Readings for a vehicle are kept in insertion order, so the last
    element is always the most recent reading.
    """

    def __init__(self) -> None:
        self._readings_by_vehicle: Dict[str, List[TelemetryReading]] = {}
        self._next_id: int = 1

    def add_reading(self, data: dict) -> TelemetryReading:
        reading = TelemetryReading(
            reading_id=self._next_id,
            recorded_at=datetime.utcnow(),
            **data,
        )
        self._readings_by_vehicle.setdefault(data["vehicle_id"], []).append(reading)
        self._next_id += 1
        return reading

    def get_all_for_vehicle(self, vehicle_id: str) -> List[TelemetryReading]:
        return self._readings_by_vehicle.get(vehicle_id, [])

    def get_latest_for_vehicle(self, vehicle_id: str) -> Optional[TelemetryReading]:
        readings = self._readings_by_vehicle.get(vehicle_id)
        if not readings:
            return None
        return readings[-1]
