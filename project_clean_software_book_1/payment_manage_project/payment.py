import abc
from typing import Dict

from .database import SalesReceipt, ServiceCharge, TimeCard


class PaymentClassification(metaclass=abc.ABCMeta):
    pass


class Affiliation(metaclass=abc.ABCMeta):
    pass


class SalariedClassification(PaymentClassification):
    def __init__(self, salary: float):
        self._salary = salary

    @property
    def salary(self) -> float:
        return self._salary


class HourlyClassification(PaymentClassification):
    def __init__(self):
        self._time_card: Dict[int, TimeCard] = {}

    def add_time_card(self, tc: TimeCard):
        self._time_card[tc.date] = tc

    def get_time_card(self, date: int) -> TimeCard:
        return self._time_card[date]


class CommissionedClassification(PaymentClassification):
    def __init__(self, salary: float):
        self._sales_receipt: Dict[int, SalesReceipt] = {}
        self._salary = salary

    @property
    def salary(self) -> float:
        return self._salary

    def add_sales_receipt(self, sr: SalesReceipt):
        self._sales_receipt[sr.date] = sr

    def get_sales_receipt(self, date: int) -> SalesReceipt:
        return self._sales_receipt[date]


class UnionAffiliation(Affiliation):
    def __init__(self, value: float):
        self._value = value
        self._service_charge: Dict[int, ServiceCharge] = {}

    @property
    def value(self) -> float:
        return self._value

    def add_service_charge(self, sc: ServiceCharge):
        self._service_charge[sc.date] = sc

    def get_service_charge(self, date: int) -> ServiceCharge:
        return self._service_charge[date]


class PaymentSchedule:
    pass


class PaymentMethod:
    pass
