from typing import NamedTuple
from datetime import datetime

class Car(NamedTuple):
    make: str
    model: str
    year: int
    color: str
    manufacture_date: datetime.date


