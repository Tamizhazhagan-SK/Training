from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from configurations.postgres_conn import get_db
from dtos.vehicle_dto import VehicleCreateRequest, VehicleResponse
from repositories.vehicle_repository import VehicleRepository
from repositories.dealer_repository import DealerRepository
from services.vehicle_service import VehicleService

vehicle_router = APIRouter(prefix="/vehicles", tags=["Vehicles"])
dealer_vehicle_router = APIRouter(prefix="/dealers", tags=["Dealers"])


def get_vehicle_service(db: Session = Depends(get_db)) -> VehicleService:
    return VehicleService(VehicleRepository(db), DealerRepository(db))


@vehicle_router.post("", response_model=VehicleResponse, status_code=status.HTTP_201_CREATED)
def create_vehicle(
    request: VehicleCreateRequest,
    service: VehicleService = Depends(get_vehicle_service),
) -> VehicleResponse:
    vehicle = service.create_vehicle(request)
    return VehicleResponse.model_validate(vehicle)


@vehicle_router.get("", response_model=List[VehicleResponse])
def list_vehicles(
    model: Optional[str] = Query(default=None, description="Filter by model, e.g. X5"),
    city: Optional[str] = Query(default=None, description="Filter by dealer city"),
    min_price: Optional[float] = Query(default=None, ge=0),
    max_price: Optional[float] = Query(default=None, ge=0),
    service: VehicleService = Depends(get_vehicle_service),
) -> List[VehicleResponse]:
    vehicles = service.get_all_vehicles(
        model=model, city=city, min_price=min_price, max_price=max_price
    )
    return [VehicleResponse.model_validate(v) for v in vehicles]


@vehicle_router.get("/{vehicle_id}", response_model=VehicleResponse)
def get_vehicle(
    vehicle_id: int,
    service: VehicleService = Depends(get_vehicle_service),
) -> VehicleResponse:
    vehicle = service.get_vehicle(vehicle_id)
    return VehicleResponse.model_validate(vehicle)


@vehicle_router.put("/{vehicle_id}/sold", response_model=VehicleResponse)
def mark_vehicle_sold(
    vehicle_id: int,
    service: VehicleService = Depends(get_vehicle_service),
) -> VehicleResponse:
    vehicle = service.mark_sold(vehicle_id)
    return VehicleResponse.model_validate(vehicle)


@dealer_vehicle_router.get("/{dealer_id}/vehicles", response_model=List[VehicleResponse])
def get_vehicles_for_dealer(
    dealer_id: int,
    service: VehicleService = Depends(get_vehicle_service),
) -> List[VehicleResponse]:
    vehicles = service.get_vehicles_for_dealer(dealer_id)
    return [VehicleResponse.model_validate(v) for v in vehicles]
