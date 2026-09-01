from fastapi import APIRouter

from dtos.telemetry_response import VehicleHealthResponse
from controllers.telemetry_controller import telemetry_service

router = APIRouter(prefix="/vehicles", tags=["Vehicle Health"])


@router.get("/{vehicle_id}/health", response_model=VehicleHealthResponse)
def get_vehicle_health(vehicle_id: str) -> VehicleHealthResponse:
    health = telemetry_service.get_health(vehicle_id)
    return VehicleHealthResponse(**health)
