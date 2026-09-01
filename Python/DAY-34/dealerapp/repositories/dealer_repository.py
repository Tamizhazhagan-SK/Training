from typing import List, Optional
from sqlalchemy.orm import Session

from models.dealer import Dealer


class DealerRepository:
    def __init__(self, db: Session) -> None:
        self._db = db

    def create(self, data: dict) -> Dealer:
        dealer = Dealer(**data)
        self._db.add(dealer)
        self._db.commit()
        self._db.refresh(dealer)
        return dealer

    def get_all(self) -> List[Dealer]:
        return self._db.query(Dealer).all()

    def get_by_id(self, dealer_id: int) -> Optional[Dealer]:
        return self._db.query(Dealer).filter(Dealer.dealer_id == dealer_id).first()
