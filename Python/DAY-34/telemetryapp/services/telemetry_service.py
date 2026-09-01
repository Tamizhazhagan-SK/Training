from typing import List
from fastapi import HTTPException, status

from repositories.telemetry_repository import TelemetryRepository
from dtos.telemetry_request import TelemetryCreateRequest
from models.telemetry import TelemetryReading
from models.health import (
    AlertType,
    EngineStatus,
    BatteryStatus,
    FuelStatus,
    OverallStatus,
    ENGINE_OVERHEAT_THRESHOLD,
    LOW_BATTERY_THRESHOLD,
    LOW_FUEL_THRESHOLD,
)


class TelemetryService:
    def __init__(self, repository: TelemetryRepository) -> None:
        self._repository = repository

    def ingest_reading(self, request: TelemetryCreateRequest) -> tuple[TelemetryReading, List[AlertType]]:
        reading = self._repository.add_reading(request.model_dump())
        alerts = self._evaluate_alerts(reading)
        return reading, alerts

    def get_history(self, vehicle_id: str) -> List[TelemetryReading]:
        return self._repository.get_all_for_vehicle(vehicle_id)

    def get_latest(self, vehicle_id: str) -> TelemetryReading:
        reading = self._repository.get_latest_for_vehicle(vehicle_id)
        if reading is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No telemetry found for vehicle '{vehicle_id}'",
            )
        return reading

    def get_health(self, vehicle_id: str) -> dict:
        reading = self.get_latest(vehicle_id)  # raises 404 if none found

        engine_status = (
            EngineStatus.OVERHEATING
            if reading.engine_temperature > ENGINE_OVERHEAT_THRESHOLD
            else EngineStatus.NORMAL
        )
        battery_status = (
            BatteryStatus.LOW
            if reading.battery_level < LOW_BATTERY_THRESHOLD
            else BatteryStatus.GOOD
        )
        fuel_status = (
            FuelStatus.LOW
            if reading.fuel_level < LOW_FUEL_THRESHOLD
            else FuelStatus.GOOD
        )

        is_healthy = (
            engine_status == EngineStatus.NORMAL
            and battery_status == BatteryStatus.GOOD
            and fuel_status == FuelStatus.GOOD
        )

        return {
            "vehicle_id": vehicle_id,
            "engine_status": engine_status,
            "battery_status": battery_status,
            "fuel_status": fuel_status,
            "overall_status": (
                OverallStatus.HEALTHY if is_healthy else OverallStatus.NEEDS_ATTENTION
            ),
        }

    @staticmethod
    def _evaluate_alerts(reading: TelemetryReading) -> List[AlertType]:
        alerts: List[AlertType] = []
        if reading.engine_temperature > ENGINE_OVERHEAT_THRESHOLD:
            alerts.append(AlertType.ENGINE_OVERHEATING)
        if reading.battery_level < LOW_BATTERY_THRESHOLD:
            alerts.append(AlertType.LOW_BATTERY)
        if reading.fuel_level < LOW_FUEL_THRESHOLD:
            alerts.append(AlertType.LOW_FUEL)
        return alerts
