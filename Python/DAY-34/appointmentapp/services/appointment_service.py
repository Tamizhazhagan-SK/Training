from datetime import date
from typing import List, Optional
from fastapi import HTTPException, status

from repositories.appointment_repository import AppointmentRepository
from dtos.appointment_request import AppointmentCreateRequest, AppointmentUpdateRequest
from models.appointment import Appointment, AppointmentStatus


class AppointmentService:
    def __init__(self, repository: AppointmentRepository) -> None:
        self._repository = repository

    def create_appointment(self, request: AppointmentCreateRequest) -> Appointment:
        if self._repository.exists_for_vin_and_date(request.vin, request.service_date):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=(
                    f"Vehicle '{request.vin}' already has an appointment "
                    f"on {request.service_date}"
                ),
            )
        return self._repository.create(request.model_dump())

    def get_all_appointments(
        self,
        status_filter: Optional[AppointmentStatus] = None,
        vin: Optional[str] = None,
    ) -> List[Appointment]:
        return self._repository.get_all(status=status_filter, vin=vin)

    def get_appointment(self, appointment_id: int) -> Appointment:
        appointment = self._repository.get_by_id(appointment_id)
        if appointment is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Appointment with id {appointment_id} not found",
            )
        return appointment

    def update_appointment(
        self, appointment_id: int, request: AppointmentUpdateRequest
    ) -> Appointment:
        # Ensures 404 is raised if it doesn't exist
        self.get_appointment(appointment_id)

        if self._repository.exists_for_vin_and_date(
            request.vin, request.service_date, exclude_id=appointment_id
        ):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=(
                    f"Vehicle '{request.vin}' already has another appointment "
                    f"on {request.service_date}"
                ),
            )

        return self._repository.update(appointment_id, request.model_dump())

    def delete_appointment(self, appointment_id: int) -> None:
        # Ensures 404 is raised if it doesn't exist
        self.get_appointment(appointment_id)
        self._repository.delete(appointment_id)
