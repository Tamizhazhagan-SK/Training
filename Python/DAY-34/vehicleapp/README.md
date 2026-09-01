# BMW Vehicle Management API

FastAPI CRUD API for managing BMW vehicles registered in a dealership system.

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

| Method | Path                | Description             |
|--------|---------------------|--------------------------|
| POST   | /vehicles            | Create a vehicle         |
| GET    | /vehicles            | List all vehicles        |
| GET    | /vehicles/{id}       | Get a vehicle by id      |
| PUT    | /vehicles/{id}       | Update a vehicle         |
| DELETE | /vehicles/{id}       | Delete a vehicle         |

## Example request

```json
{
  "vin": "BMWX5VIN001",
  "model": "BMW X5",
  "year": 2026,
  "fuel_type": "Petrol",
  "color": "Black",
  "price": 9500000
}
```

## Notes

- Storage is in-memory (`repositories/vehicle_repository.py`) — data resets on restart.
  Swap it for a SQLAlchemy repository later without touching the service/controller layers.
- `GET /vehicles/{id}` and `PUT/DELETE /vehicles/{id}` return `404` when the vehicle doesn't exist.
- Duplicate VINs are rejected with `409 Conflict`.
