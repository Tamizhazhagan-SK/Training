from typing import List
from fastapi import APIRouter, status

from dtos.telemetry_request import TelemetryCreateRequest
from dtos.telemetry_response import TelemetryResponse, TelemetryIngestResponse, AlertResponse
from repositories.telemetry_repository import TelemetryRepository
from services.telemetry_service import TelemetryService

router = APIRouter(prefix="/telemetry", tags=["Telemetry"])

# Shared instances (also imported by the health controller).
telemetry_repository = TelemetryRepository()
telemetry_service = TelemetryService(telemetry_repository)


@router.post("", response_model=TelemetryIngestResponse, status_code=status.HTTP_201_CREATED)
def submit_telemetry(request: TelemetryCreateRequest) -> TelemetryIngestResponse:
    reading, alerts = telemetry_service.ingest_reading(request)
    return TelemetryIngestResponse(
        reading=TelemetryResponse.model_validate(reading),
        alerts=[AlertResponse(vehicle_id=reading.vehicle_id, alert=a) for a in alerts],
    )


@router.get("/{vehicle_id}", response_model=List[TelemetryResponse])
def get_telemetry_history(vehicle_id: str) -> List[TelemetryResponse]:
    readings = telemetry_service.get_history(vehicle_id)
    return [TelemetryResponse.model_validate(r) for r in readings]


@router.get("/{vehicle_id}/latest", response_model=TelemetryResponse)
def get_latest_telemetry(vehicle_id: str) -> TelemetryResponse:
    reading = telemetry_service.get_latest(vehicle_id)
    return TelemetryResponse.model_validate(reading)
