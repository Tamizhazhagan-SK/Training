from pydantic import BaseModel, Field


class DealerCreateRequest(BaseModel):
    dealer_name: str = Field(..., min_length=2, max_length=100)
    city: str = Field(..., min_length=2, max_length=50)

    class Config:
        json_schema_extra = {
            "example": {"dealer_name": "BMW Chennai", "city": "Chennai"}
        }


class DealerResponse(BaseModel):
    dealer_id: int
    dealer_name: str
    city: str

    class Config:
        from_attributes = True
