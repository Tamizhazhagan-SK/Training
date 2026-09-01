# BMW Roadside Assistance API

Handles roadside assistance requests raised from the BMW mobile app: request
creation, technician assignment, and status tracking through to completion.

## Setup

```bash
pip install -e .
# or without the pyproject: pip install fastapi "uvicorn[standard]" pydantic
```

## Run

```bash
uvicorn main:app --reload
```

Swagger UI: http://127.0.0.1:8000/docs

## Endpoints

| Method | Path                                  | Description                          |
|--------|-----------------------------------------|-----------------------------------------|
| POST   | /roadside-assistance                    | Raise a new request                    |
| GET    | /roadside-assistance/{request_id}       | Get a request by id                    |
| PUT    | /roadside-assistance/{request_id}/assign| Assign a technician                    |
| PUT    | /roadside-assistance/{request_id}/status| Move the request to a new status       |

## Example request

```json
// POST /roadside-assistance
{
  "vehicle_id": "BMW001",
  "vin": "BMWVIN00981",
  "issue": "Flat tyre",
  "latitude": 13.0827,
  "longitude": 80.2707
}
```

Response:

```json
{
  "request_id": 5001,
  "vehicle_id": "BMW001",
  "status": "REQUESTED",
  "estimated_arrival_minutes": 25,
  "...": "..."
}
```

`estimated_arrival_minutes` is a random value between 10–45 for the demo
(`services/roadside_request_service.py::_estimate_arrival_minutes`) — swap
in real distance/traffic logic later without touching the controller.

## Status lifecycle

```
REQUESTED --assign--> ASSIGNED --status--> IN_PROGRESS --status--> COMPLETED
    |                     |                      |
    +---------------- status: CANCELLED ---------+
```

Rules enforced in `models/status.py` (`ALLOWED_TRANSITIONS`) and
`services/roadside_request_service.py`:

- A request must be `REQUESTED` to be assigned via `PUT .../assign`
  (`409` otherwise, e.g. assigning twice).
- `ASSIGNED` can only be reached through `PUT .../assign`, not through the
  generic `PUT .../status` endpoint.
- `PUT .../status` only allows moves defined in `ALLOWED_TRANSITIONS`:
  `REQUESTED → CANCELLED`, `ASSIGNED → IN_PROGRESS/CANCELLED`,
  `IN_PROGRESS → COMPLETED/CANCELLED`. `COMPLETED` and `CANCELLED` are
  terminal — any further update returns `409`.

## Notes

- Storage is in-memory (`repositories/roadside_request_repository.py`) —
  data resets on restart. Request ids start at `5001` to match the
  exercise's example.
- `GET/PUT .../{request_id}...` return `404` when the request doesn't exist.
