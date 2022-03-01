from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict, Optional

if TYPE_CHECKING:
    from .payment import PaymentClassification, PaymentMethod, PaymentSchedule

logger = logging.getLogger(__name__)


@dataclass
class Employee:
    empid: int
    address: str
    name: str

    @property
    def classification(self) -> PaymentClassification:
        return self._pc

    @classification.setter
    def classification(self, pc: PaymentClassification):
        self._pc = pc

    @property
    def schedule(self) -> PaymentSchedule:
        return self._ps

    @schedule.setter
    def schedule(self, ps: PaymentSchedule):
        self._ps = ps

    @property
    def method(self) -> PaymentMethod:
        return self._pm

    @method.setter
    def method(self, pm: PaymentMethod):
        self._pm = pm


@dataclass
class TimeCard:
    date: int
    hourly: float


class PayrollDatabase:
    """
    pacade pattern?
    """

    def __init__(self):
        self._employee: Dict[int, Employee] = {}

    def add_employee(self, empid: int, e: Employee):
        self._employee[empid] = e

    def delete_employee(self, empid: int):
        del self._employee[empid]

    def get_employee(self, empid: int) -> Employee:
        return self._employee[empid]

    def get_or_none_employee(self, empid: int) -> Optional[Employee]:
        try:
            return self._employee[empid]
        except KeyError:
            logger.info("no empid: %s", empid)
            return None

    def clear(self):
        self._employee.clear()


GpayrollDatabase = PayrollDatabase()
