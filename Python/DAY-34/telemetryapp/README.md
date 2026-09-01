# BMW Connected Car Sensor API

Ingests telemetry from connected BMW vehicles and derives per-vehicle health
and alerts.

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

| Method | Path                          | Description                                   |
|--------|-------------------------------|------------------------------------------------|
| POST   | /telemetry                     | Submit a sensor reading (returns any alerts)  |
| GET    | /telemetry/{vehicle_id}        | Full telemetry history for a vehicle          |
| GET    | /telemetry/{vehicle_id}/latest | Most recent reading for a vehicle             |
| GET    | /vehicles/{vehicle_id}/health  | Derived health status for a vehicle           |

## Example request

```json
{
  "vehicle_id": "BMW001",
  "speed": 92,
  "engine_temperature": 98,
  "battery_level": 72,
  "fuel_level": 35,
  "latitude": 13.0827,
  "longitude": 80.2707
}
```

## Alert & health thresholds

Defined in `models/health.py`:

- `engine_temperature > 110` → `ENGINE_OVERHEATING`, engine status `OVERHEATING`
- `battery_level < 15` → `LOW_BATTERY`, battery status `LOW`
- `fuel_level < 10` → `LOW_FUEL`, fuel status `LOW`

`POST /telemetry` evaluates the submitted reading and returns any alerts it
triggered alongside the stored reading, e.g.:

```json
{
  "reading": { "...": "..." },
  "alerts": [
    { "vehicle_id": "BMW001", "alert": "ENGINE_OVERHEATING" }
  ]
}
```

`GET /vehicles/{vehicle_id}/health` derives status from the **latest**
reading only:

```json
{
  "vehicle_id": "BMW001",
  "engine_status": "NORMAL",
  "battery_status": "GOOD",
  "fuel_status": "GOOD",
  "overall_status": "HEALTHY"
}
```

`overall_status` is `HEALTHY` only if engine, battery, and fuel are all
within normal range; otherwise `NEEDS_ATTENTION`.

## Notes

- Storage is in-memory (`repositories/telemetry_repository.py`), grouped by
  `vehicle_id` in insertion order — data resets on restart.
- Requesting history, latest reading, or health for a vehicle with no
  telemetry returns `404`.
