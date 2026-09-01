from fastapi import APIRouter, status

from dtos.roadside_request_dto import (
    RoadsideRequestCreate,
    AssignTechnicianRequest,
    StatusUpdateRequest,
)
from dtos.roadside_response_dto import RoadsideRequestResponse
from repositories.roadside_request_repository import RoadsideRequestRepository
from services.roadside_request_service import RoadsideRequestService

router = APIRouter(prefix="/roadside-assistance", tags=["Roadside Assistance"])

# Single shared instances for this in-memory demo app.
_repository = RoadsideRequestRepository()
_service = RoadsideRequestService(_repository)


@router.post("", response_model=RoadsideRequestResponse, status_code=status.HTTP_201_CREATED)
def request_roadside_assistance(
    request: RoadsideRequestCreate,
) -> RoadsideRequestResponse:
    created = _service.create_request(request)
    return RoadsideRequestResponse.model_validate(created)


@router.get("/{request_id}", response_model=RoadsideRequestResponse)
def get_roadside_request(request_id: int) -> RoadsideRequestResponse:
    req = _service.get_request(request_id)
    return RoadsideRequestResponse.model_validate(req)


@router.put("/{request_id}/assign", response_model=RoadsideRequestResponse)
def assign_technician(
    request_id: int, assignment: AssignTechnicianRequest
) -> RoadsideRequestResponse:
    updated = _service.assign_technician(request_id, assignment)
    return RoadsideRequestResponse.model_validate(updated)


@router.put("/{request_id}/status", response_model=RoadsideRequestResponse)
def update_status(
    request_id: int, status_update: StatusUpdateRequest
) -> RoadsideRequestResponse:
    updated = _service.update_status(request_id, status_update)
    return RoadsideRequestResponse.model_validate(updated)
