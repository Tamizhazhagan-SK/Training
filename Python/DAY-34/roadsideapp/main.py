from fastapi import FastAPI

from controllers.roadside_request_controller import router as roadside_router

app = FastAPI(
    title="BMW Roadside Assistance API",
    description="Handles roadside assistance requests raised from the BMW mobile app.",
    version="1.0.0",
)

app.include_router(roadside_router)


@app.get("/", tags=["Health"])
def root():
    return {"status": "ok", "service": "BMW Roadside Assistance API"}


# Run with: uvicorn main:app --reload
# Swagger UI available at: http://127.0.0.1:8000/docs
