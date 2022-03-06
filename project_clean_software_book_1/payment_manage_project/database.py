from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict, Optional

if TYPE_CHECKING:
    from .payment import (
        Affiliation,
        PaymentClassification,
        PaymentMethod,
        PaymentSchedule,
    )

logger = logging.getLogger(__name__)


@dataclass
class Employee:
    emp_id: int
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

    @property
    def affiliation(self) -> Affiliation:
        return self._af

    @affiliation.setter
    def affiliation(self, af: Affiliation):
        self._af = af


@dataclass
class TimeCard:
    date: int
    hourly: float


@dataclass
class SalesReceipt:
    date: int
    amount: float


@dataclass
class ServiceCharge:
    date: int
    amount: float


class PayrollDatabase:
    """
    pacade pattern?
    """

    def __init__(self):
        self._employee: Dict[int, Employee] = {}
        self._member: Dict[int, Employee] = {}

    def add_employee(self, emp_id: int, e: Employee):
        self._employee[emp_id] = e

    def add_union_member(self, member_id: int, e: Employee):
        self._member[member_id] = e

    def delete_employee(self, emp_id: int):
        del self._employee[emp_id]

    def get_employee(self, emp_id: int) -> Employee:
        return self._employee[emp_id]

    def get_union_member(self, member_id: int) -> Employee:
        return self._member[member_id]

    def get_or_none_employee(self, emp_id: int) -> Optional[Employee]:
        try:
            return self._employee[emp_id]
        except KeyError:
            logger.info("no emp_id: %s", emp_id)
            return None

    def clear(self):
        self._employee.clear()


GpayrollDatabase = PayrollDatabase()
