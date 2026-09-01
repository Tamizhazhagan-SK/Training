from fastapi import FastAPI

from controllers.appointment_controller import router as appointment_router

app = FastAPI(
    title="BMW Service Appointment API",
    description="API for scheduling BMW vehicle service appointments.",
    version="1.0.0",
)

app.include_router(appointment_router)


@app.get("/", tags=["Health"])
def root():
    return {"status": "ok", "service": "BMW Service Appointment API"}


# Run with: uvicorn main:app --reload
# Swagger UI available at: http://127.0.0.1:8000/docs
