from datetime import date
from typing import Dict, List, Optional
from models.appointment import Appointment, AppointmentStatus


class AppointmentRepository:
    """Simple in-memory 'database' for service appointments."""

    def __init__(self) -> None:
        self._appointments: Dict[int, Appointment] = {}
        self._next_id: int = 1

    def create(self, data: dict) -> Appointment:
        appointment = Appointment(appointment_id=self._next_id, **data)
        self._appointments[self._next_id] = appointment
        self._next_id += 1
        return appointment

    def get_all(
        self,
        status: Optional[AppointmentStatus] = None,
        vin: Optional[str] = None,
    ) -> List[Appointment]:
        results = list(self._appointments.values())
        if status is not None:
            results = [a for a in results if a.status == status]
        if vin is not None:
            results = [a for a in results if a.vin == vin]
        return results

    def get_by_id(self, appointment_id: int) -> Optional[Appointment]:
        return self._appointments.get(appointment_id)

    def update(self, appointment_id: int, data: dict) -> Optional[Appointment]:
        if appointment_id not in self._appointments:
            return None
        updated = Appointment(appointment_id=appointment_id, **data)
        self._appointments[appointment_id] = updated
        return updated

    def delete(self, appointment_id: int) -> bool:
        if appointment_id not in self._appointments:
            return False
        del self._appointments[appointment_id]
        return True

    def exists_for_vin_and_date(
        self,
        vin: str,
        service_date: date,
        exclude_id: Optional[int] = None,
    ) -> bool:
        """Business rule: no two appointments for the same VIN on the same date."""
        return any(
            a.vin == vin and a.service_date == service_date
            for aid, a in self._appointments.items()
            if aid != exclude_id
        )
