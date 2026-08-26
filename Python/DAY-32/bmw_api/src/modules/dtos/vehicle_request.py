from pydantic import BaseModel, Field


class VehicleRequest(BaseModel):
    """
    VehicleRequest is a Pydantic model that represents a request for vehicle information.
    It includes the following fields:
    - vehicle_id: An integer representing the unique identifier of the vehicle.
    - make: A string representing the manufacturer of the vehicle.
    - model: A string representing the model of the vehicle.
    - year: An integer representing the year of manufacture of the vehicle.
    """

    make: str = Field(..., min_length=1, max_length=50, pattern="^[a-zA-Z0-9 ]+$", description="The manufacturer of the vehicle.")
    model: str = Field(..., min_length=1, max_length=50, pattern="^[a-zA-Z0-9 ]+$", description="The model of the vehicle.")
    year: int = Field(..., ge=1900, le=2100, description="The year of manufacture of the vehicle.")
    vin: str = Field(..., min_length=17, max_length=17, pattern="^[A-HJ-NPR-Z0-9]{17}$", description="The Vehicle Identification Number (VIN).")
    