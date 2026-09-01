from enum import Enum
from typing import Dict, Set


class RequestStatus(str, Enum):
    REQUESTED = "REQUESTED"
    ASSIGNED = "ASSIGNED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


# Which statuses a request may move to next, from its current status.
# ASSIGNED is reached only via the dedicated /assign endpoint, not via
# the generic /status endpoint.
ALLOWED_TRANSITIONS: Dict[RequestStatus, Set[RequestStatus]] = {
    RequestStatus.REQUESTED: {RequestStatus.CANCELLED},
    RequestStatus.ASSIGNED: {RequestStatus.IN_PROGRESS, RequestStatus.CANCELLED},
    RequestStatus.IN_PROGRESS: {RequestStatus.COMPLETED, RequestStatus.CANCELLED},
    RequestStatus.COMPLETED: set(),
    RequestStatus.CANCELLED: set(),
}
