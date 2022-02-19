import logging
from dataclasses import dataclass
from typing import Dict, Optional

from .payment import PaymentClassification, PaymentMethod, PaymentSchedule

logger = logging.getLogger(__name__)


@dataclass
class Employee:
    _id: int
    address: str
    name: str

    def set_classification(self, pc: PaymentClassification):
        self._pc = pc

    def get_classification(self) -> PaymentClassification:
        return self._pc

    def set_schedule(self, ps: PaymentSchedule):
        self._ps = ps

    def get_schedule(self) -> PaymentSchedule:
        return self._ps

    def set_method(self, pm: PaymentMethod):
        self._pm = pm

    def get_method(self) -> PaymentMethod:
        return self._pm


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
