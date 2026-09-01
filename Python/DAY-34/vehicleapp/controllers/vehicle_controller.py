from typing import List
from fastapi import APIRouter, status

from dtos.vehicle_request import VehicleCreateRequest, VehicleUpdateRequest
from dtos.vehicle_response import VehicleResponse
from repositories.vehicle_repository import VehicleRepository
from services.vehicle_service import VehicleService

router = APIRouter(prefix="/vehicles", tags=["Vehicles"])

# Single shared instances for this in-memory demo app.
_repository = VehicleRepository()
_service = VehicleService(_repository)


@router.post("", response_model=VehicleResponse, status_code=status.HTTP_201_CREATED)
def create_vehicle(request: VehicleCreateRequest) -> VehicleResponse:
    vehicle = _service.create_vehicle(request)
    return VehicleResponse.model_validate(vehicle)


@router.get("", response_model=List[VehicleResponse])
def list_vehicles() -> List[VehicleResponse]:
    vehicles = _service.get_all_vehicles()
    return [VehicleResponse.model_validate(v) for v in vehicles]


@router.get("/{vehicle_id}", response_model=VehicleResponse)
def get_vehicle(vehicle_id: int) -> VehicleResponse:
    vehicle = _service.get_vehicle(vehicle_id)
    return VehicleResponse.model_validate(vehicle)


@router.put("/{vehicle_id}", response_model=VehicleResponse)
def update_vehicle(vehicle_id: int, request: VehicleUpdateRequest) -> VehicleResponse:
    vehicle = _service.update_vehicle(vehicle_id, request)
    return VehicleResponse.model_validate(vehicle)


@router.delete("/{vehicle_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vehicle(vehicle_id: int) -> None:
    _service.delete_vehicle(vehicle_id)
