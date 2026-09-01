from fastapi import FastAPI

from controllers.vehicle_controller import router as vehicle_router

app = FastAPI(
    title="BMW Vehicle Management API",
    description="CRUD API for managing BMW vehicles registered in a dealership system.",
    version="1.0.0",
)

app.include_router(vehicle_router)


@app.get("/", tags=["Health"])
def root():
    return {"status": "ok", "service": "BMW Vehicle Management API"}


# Run with: uvicorn main:app --reload
# Swagger UI available at: http://127.0.0.1:8000/docs
