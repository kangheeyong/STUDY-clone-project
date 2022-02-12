from dataclasses import dataclass
from typing import Dict

from .payment import PaymentClassification, PaymentMethod, PaymentSchedule


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

    _employee: Dict[int, Employee] = {}

    @classmethod
    def add_employee(cls, empid: int, e: Employee):
        cls._employee[empid] = e

    @classmethod
    def get_employee(cls, empid: int) -> Employee:
        return cls._employee[empid]

    @classmethod
    def clear(cls):
        cls._employee.clear()
