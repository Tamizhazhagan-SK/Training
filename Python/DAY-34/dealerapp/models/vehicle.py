import enum
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum as SAEnum
from sqlalchemy.orm import relationship

from configurations.postgres_conn import Base


class VehicleStatus(str, enum.Enum):
    AVAILABLE = "AVAILABLE"
    SOLD = "SOLD"


class Vehicle(Base):
    __tablename__ = "vehicles"

    vehicle_id = Column(Integer, primary_key=True, autoincrement=True)
    vin = Column(String(30), nullable=False, unique=True, index=True)
    model = Column(String(50), nullable=False, index=True)
    price = Column(Float, nullable=False)
    dealer_id = Column(Integer, ForeignKey("dealers.dealer_id"), nullable=False)
    status = Column(
        SAEnum(VehicleStatus, name="vehicle_status"),
        nullable=False,
        default=VehicleStatus.AVAILABLE,
    )

    dealer = relationship("Dealer", back_populates="vehicles")
