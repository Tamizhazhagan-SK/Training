from fastapi import FastAPI

from configurations.postgres_conn import init_db
from controllers.dealer_controller import router as dealer_router
from controllers.vehicle_controller import vehicle_router, dealer_vehicle_router

app = FastAPI(
    title="BMW Dealer Inventory API",
    description="Manages BMW vehicle inventories across dealerships, backed by PostgreSQL.",
    version="1.0.0",
)

app.include_router(dealer_router)
app.include_router(vehicle_router)
app.include_router(dealer_vehicle_router)


@app.on_event("startup")
def on_startup() -> None:
    init_db()


@app.get("/", tags=["Health"])
def root():
    return {"status": "ok", "service": "BMW Dealer Inventory API"}


# Run with: uvicorn main:app --reload
# Swagger UI available at: http://127.0.0.1:8000/docs
