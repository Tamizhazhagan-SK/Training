# BMW Dealer Inventory API

FastAPI + PostgreSQL API for managing BMW vehicle inventories across dealerships.

## Project structure

```
dealerapp/
├── controllers/
│   ├── dealer_controller.py
│   └── vehicle_controller.py
├── services/
│   ├── dealer_service.py
│   └── vehicle_service.py
├── repositories/
│   ├── dealer_repository.py
│   └── vehicle_repository.py
├── models/
│   ├── dealer.py            # SQLAlchemy ORM model
│   └── vehicle.py           # SQLAlchemy ORM model, FK to Dealer
├── dtos/
│   ├── dealer_dto.py
│   └── vehicle_dto.py
├── configurations/
│   └── postgres_conn.py     # engine, session, get_db dependency
├── main.py
├── pyproject.toml
├── docker-compose.yml       # local Postgres for development
└── .env.example
```

## Setup

### 1. Start Postgres

```bash
docker compose up -d
```

This starts Postgres on `localhost:5432` with database `bmw_dealer_inventory`,
user/password `postgres`/`postgres` (matches the default in
`configurations/postgres_conn.py`).

Don't have Docker? Point `DATABASE_URL` at any Postgres instance you have,
or use SQLite for quick local testing (see **Notes** below).

### 2. Install dependencies

```bash
pip install -e .
```

### 3. Run

```bash
uvicorn main:app --reload
```

Tables are created automatically on startup (`init_db()` in
`configurations/postgres_conn.py`). Swagger UI: http://127.0.0.1:8000/docs

## Endpoints

| Method | Path                              | Description                              |
|--------|-------------------------------------|--------------------------------------------|
| POST   | /dealers                            | Create a dealer                            |
| GET    | /dealers                            | List dealers                               |
| POST   | /vehicles                           | Create a vehicle                           |
| GET    | /vehicles                           | List vehicles (filterable)                 |
| GET    | /vehicles/{vehicle_id}              | Get a vehicle by id                        |
| GET    | /dealers/{dealer_id}/vehicles       | Vehicles for one dealer                    |
| PUT    | /vehicles/{vehicle_id}/sold         | Transition AVAILABLE → SOLD                |

Vehicle filters (combinable): `?model=X5`, `?city=Chennai` (joins to the
dealer's city), `?min_price=5000000&max_price=10000000`.

## Example requests

```json
// POST /dealers
{ "dealer_name": "BMW Chennai", "city": "Chennai" }

// POST /vehicles
{
  "vin": "BMWIX001",
  "model": "BMW iX",
  "price": 12500000,
  "dealer_id": 101,
  "status": "AVAILABLE"
}
```

## The sold challenge

`PUT /vehicles/{vehicle_id}/sold` flips a vehicle from `AVAILABLE` to
`SOLD` inside a transaction (`repositories/vehicle_repository.py::mark_sold`),
rolling back on any DB error. It returns:
- `404` if the vehicle doesn't exist
- `409` if it isn't currently `AVAILABLE` (e.g. already `SOLD`)

## Notes

- `VehicleService.create_vehicle` checks the dealer exists (`404` if not)
  and rejects duplicate VINs (`409`).
- `GET /dealers/{dealer_id}/vehicles` returns `404` if the dealer doesn't exist.
- For quick local testing without Postgres, `configurations/postgres_conn.py`
  reads `DATABASE_URL` from the environment — set it to a SQLite URL, e.g.
  `export DATABASE_URL=sqlite:////tmp/bmw_dealer.db`. Same models, same
  code path; swap back to Postgres for the actual exercise.
