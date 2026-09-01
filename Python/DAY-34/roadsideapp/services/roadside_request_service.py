import random
from fastapi import HTTPException, status as http_status

from repositories.roadside_request_repository import RoadsideRequestRepository
from dtos.roadside_request_dto import (
    RoadsideRequestCreate,
    AssignTechnicianRequest,
    StatusUpdateRequest,
)
from models.roadside_request import RoadsideRequest
from models.status import RequestStatus, ALLOWED_TRANSITIONS

MIN_ETA_MINUTES = 10
MAX_ETA_MINUTES = 45


class RoadsideRequestService:
    def __init__(self, repository: RoadsideRequestRepository) -> None:
        self._repository = repository

    def create_request(self, request: RoadsideRequestCreate) -> RoadsideRequest:
        eta = self._estimate_arrival_minutes()
        return self._repository.create(request.model_dump(), eta)

    def get_request(self, request_id: int) -> RoadsideRequest:
        req = self._repository.get_by_id(request_id)
        if req is None:
            raise HTTPException(
                status_code=http_status.HTTP_404_NOT_FOUND,
                detail=f"Roadside assistance request {request_id} not found",
            )
        return req

    def assign_technician(
        self, request_id: int, assignment: AssignTechnicianRequest
    ) -> RoadsideRequest:
        req = self.get_request(request_id)

        if req.status != RequestStatus.REQUESTED:
            raise HTTPException(
                status_code=http_status.HTTP_409_CONFLICT,
                detail=(
                    f"Request {request_id} cannot be assigned from status "
                    f"'{req.status.value}' (must be REQUESTED)"
                ),
            )

        updated = req.model_copy(
            update={
                "status": RequestStatus.ASSIGNED,
                "technician_id": assignment.technician_id,
                "technician_name": assignment.technician_name,
            }
        )
        return self._repository.save(updated)

    def update_status(
        self, request_id: int, status_update: StatusUpdateRequest
    ) -> RoadsideRequest:
        req = self.get_request(request_id)
        new_status = status_update.status

        allowed_next = ALLOWED_TRANSITIONS.get(req.status, set())
        if new_status not in allowed_next:
            raise HTTPException(
                status_code=http_status.HTTP_409_CONFLICT,
                detail=(
                    f"Cannot move request {request_id} from '{req.status.value}' "
                    f"to '{new_status.value}'"
                ),
            )

        updated = req.model_copy(update={"status": new_status})
        return self._repository.save(updated)

    @staticmethod
    def _estimate_arrival_minutes() -> int:
        # In a real system this would factor in technician location,
        # traffic, and distance. Kept simple for the exercise.
        return random.randint(MIN_ETA_MINUTES, MAX_ETA_MINUTES)
