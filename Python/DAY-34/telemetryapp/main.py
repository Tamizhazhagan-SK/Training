from fastapi import FastAPI

from controllers.telemetry_controller import router as telemetry_router
from controllers.health_controller import router as health_router

app = FastAPI(
    title="BMW Connected Car Sensor API",
    description="Receives telemetry from connected BMW vehicles and derives health/alerts.",
    version="1.0.0",
)

app.include_router(telemetry_router)
app.include_router(health_router)


@app.get("/", tags=["Health"])
def root():
    return {"status": "ok", "service": "BMW Connected Car Sensor API"}


# Run with: uvicorn main:app --reload
# Swagger UI available at: http://127.0.0.1:8000/docs
