from typing import List
from fastapi import HTTPException, status

from repositories.dealer_repository import DealerRepository
from dtos.dealer_dto import DealerCreateRequest
from models.dealer import Dealer


class DealerService:
    def __init__(self, repository: DealerRepository) -> None:
        self._repository = repository

    def create_dealer(self, request: DealerCreateRequest) -> Dealer:
        return self._repository.create(request.model_dump())

    def get_all_dealers(self) -> List[Dealer]:
        return self._repository.get_all()

    def get_dealer(self, dealer_id: int) -> Dealer:
        dealer = self._repository.get_by_id(dealer_id)
        if dealer is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Dealer with id {dealer_id} not found",
            )
        return dealer
