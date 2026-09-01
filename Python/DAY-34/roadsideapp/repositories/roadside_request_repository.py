from datetime import datetime
from typing import Dict, Optional
from models.roadside_request import RoadsideRequest
from models.status import RequestStatus


class RoadsideRequestRepository:
    def __init__(self) -> None:
        self._requests: Dict[int, RoadsideRequest] = {}
        self._next_id: int = 5001  # matches the exercise's example request_id

    def create(self, data: dict, estimated_arrival_minutes: int) -> RoadsideRequest:
        request = RoadsideRequest(
            request_id=self._next_id,
            status=RequestStatus.REQUESTED,
            estimated_arrival_minutes=estimated_arrival_minutes,
            created_at=datetime.utcnow(),
            **data,
        )
        self._requests[self._next_id] = request
        self._next_id += 1
        return request

    def get_by_id(self, request_id: int) -> Optional[RoadsideRequest]:
        return self._requests.get(request_id)

    def save(self, request: RoadsideRequest) -> RoadsideRequest:
        self._requests[request.request_id] = request
        return request
