# call controller and create models
from modules.configurations.psql_connection import base, engine
from modules.controllers.vehicle_controller import router
from modules.models.vehicle import Vehicle

from fastapi import FastAPI

# This is the main FastAPI application entry point.
# When the server starts, FastAPI loads all route definitions registered here.
api = FastAPI(
    title="Vehicle Management API",
    description="API for managing vehicles",
    version="1.0",
)

# generate the tables in the database
base.metadata.create_all(bind=engine)

# include the controller router
api.include_router(router)

# Request flow:
# 1. Client sends an HTTP request (GET/POST/PUT/DELETE).
# 2. FastAPI matches the URL path and method to a controller function.
# 3. The controller receives the request body/params and calls the service layer.
# 4. The service layer handles business logic and calls the repository.
# 5. The repository interacts with the database using SQLAlchemy.
# 6. The repository returns model objects (like Vehicle) to the service.
# 7. The service converts database model objects into DTOs such as VehicleResponse.
# 8. The controller returns that response object to FastAPI.
# 9. FastAPI serializes the response to JSON and sends it back to the client.
#
# Example request flow for create_vehicle():
# Client -> POST /vehicles/v1.0/ -> vehicle_controller.create_vehicle()
# -> VehicleServiceImpl.create_vehicle()
# -> VehicleRepositoryImpl.create_vehicle()
# -> SQLAlchemy inserts a row into the vehicle table
# -> repository returns the created Vehicle object
# -> service maps it to VehicleResponse
# -> controller returns VehicleResponse
# -> FastAPI sends JSON response to client
