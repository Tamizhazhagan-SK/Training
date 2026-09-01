# BMW Service Appointment API

API for scheduling BMW vehicle service appointments.

## Setup

```bash
pip install -e .
# or without the pyproject: pip install fastapi "uvicorn[standard]" pydantic
```

## Run

```bash
uvicorn main:app --reload
```

Then open Swagger UI at: http://127.0.0.1:8000/docs

## Endpoints

| Method | Path                          | Description                          |
|--------|-------------------------------|---------------------------------------|
| POST   | /appointments                  | Create an appointment                 |
| GET    | /appointments                  | List appointments                     |
| GET    | /appointments?status=SCHEDULED | Filter by status                      |
| GET    | /appointments?vin=BMWX3001     | Filter by VIN                         |
| GET    | /appointments/{id}             | Get an appointment by id              |
| PUT    | /appointments/{id}             | Update an appointment                 |
| DELETE | /appointments/{id}             | Delete an appointment                 |

Status and VIN filters can be combined: `/appointments?status=SCHEDULED&vin=BMWX3001`.

## Example request

```json
{
  "vin": "BMWX3001",
  "customer_name": "Arun Kumar",
  "service_type": "Periodic Service",
  "service_date": "2026-09-10",
  "service_center": "BMW Chennai",
  "status": "SCHEDULED"
}
```

## Business rule

A vehicle (VIN) cannot have two appointments on the same `service_date`.
Violating this on create or update returns `409 Conflict`. This is enforced in
`repositories/appointment_repository.py::exists_for_vin_and_date` and checked
by `services/appointment_service.py`.

## Notes

- Storage is in-memory (`repositories/appointment_repository.py`) — data resets on restart.
- `GET/PUT/DELETE /appointments/{id}` return `404` when the appointment doesn't exist.
