from typing import List, Optional
from fastapi import APIRouter, Query, status

from dtos.appointment_request import AppointmentCreateRequest, AppointmentUpdateRequest
from dtos.appointment_response import AppointmentResponse
from models.appointment import AppointmentStatus
from repositories.appointment_repository import AppointmentRepository
from services.appointment_service import AppointmentService

router = APIRouter(prefix="/appointments", tags=["Appointments"])

# Single shared instances for this in-memory demo app.
_repository = AppointmentRepository()
_service = AppointmentService(_repository)


@router.post("", response_model=AppointmentResponse, status_code=status.HTTP_201_CREATED)
def create_appointment(request: AppointmentCreateRequest) -> AppointmentResponse:
    appointment = _service.create_appointment(request)
    return AppointmentResponse.model_validate(appointment)


@router.get("", response_model=List[AppointmentResponse])
def list_appointments(
    status: Optional[AppointmentStatus] = Query(default=None, description="Filter by status"),
    vin: Optional[str] = Query(default=None, description="Filter by VIN"),
) -> List[AppointmentResponse]:
    appointments = _service.get_all_appointments(status_filter=status, vin=vin)
    return [AppointmentResponse.model_validate(a) for a in appointments]


@router.get("/{appointment_id}", response_model=AppointmentResponse)
def get_appointment(appointment_id: int) -> AppointmentResponse:
    appointment = _service.get_appointment(appointment_id)
    return AppointmentResponse.model_validate(appointment)


@router.put("/{appointment_id}", response_model=AppointmentResponse)
def update_appointment(
    appointment_id: int, request: AppointmentUpdateRequest
) -> AppointmentResponse:
    appointment = _service.update_appointment(appointment_id, request)
    return AppointmentResponse.model_validate(appointment)


@router.delete("/{appointment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_appointment(appointment_id: int) -> None:
    _service.delete_appointment(appointment_id)
