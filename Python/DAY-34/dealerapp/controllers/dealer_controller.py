from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from configurations.postgres_conn import get_db
from dtos.dealer_dto import DealerCreateRequest, DealerResponse
from repositories.dealer_repository import DealerRepository
from services.dealer_service import DealerService

router = APIRouter(prefix="/dealers", tags=["Dealers"])


def get_dealer_service(db: Session = Depends(get_db)) -> DealerService:
    return DealerService(DealerRepository(db))


@router.post("", response_model=DealerResponse, status_code=status.HTTP_201_CREATED)
def create_dealer(
    request: DealerCreateRequest,
    service: DealerService = Depends(get_dealer_service),
) -> DealerResponse:
    dealer = service.create_dealer(request)
    return DealerResponse.model_validate(dealer)


@router.get("", response_model=List[DealerResponse])
def list_dealers(
    service: DealerService = Depends(get_dealer_service),
) -> List[DealerResponse]:
    dealers = service.get_all_dealers()
    return [DealerResponse.model_validate(d) for d in dealers]
