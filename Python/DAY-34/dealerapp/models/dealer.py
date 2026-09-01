from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from configurations.postgres_conn import Base


class Dealer(Base):
    __tablename__ = "dealers"

    dealer_id = Column(Integer, primary_key=True, autoincrement=True)
    dealer_name = Column(String(100), nullable=False)
    city = Column(String(50), nullable=False, index=True)

    vehicles = relationship(
        "Vehicle",
        back_populates="dealer",
        cascade="all, delete-orphan",
    )
