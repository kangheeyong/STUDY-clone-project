import abc

from .database import Employee, GpayrollDatabase, SalesReceipt, ServiceCharge, TimeCard
from .payment import (
    CommissionedClassification,
    HourlyClassification,
    PaymentClassification,
    PaymentMethod,
    PaymentSchedule,
    SalariedClassification,
    UnionAffiliation,
)


class Transaction(metaclass=abc.ABCMeta):
    """
    Design Pattern: Command pattern
    """

    @abc.abstractmethod
    def execute(self):
        pass


class AddEmployeeTransaction(Transaction):
    def __init__(
        self,
        emp_id: int,
        name: str,
        address: str,
    ):
        self._emp_id = emp_id
        self._name = name
        self._address = address

    def _get_classification(self) -> PaymentClassification:
        raise NotImplementedError()

    def _get_schedule(self) -> PaymentSchedule:
        raise NotImplementedError()

    def execute(self):
        e = Employee(
            emp_id=self._emp_id,
            name=self._name,
            address=self._address,
        )

        pc = self._get_classification()
        e.classification = pc

        ps = self._get_schedule()
        e.schedule = ps

        pm = PaymentMethod()
        e.method = pm

        GpayrollDatabase.add_employee(self._emp_id, e)


class AddSalariedEmployee(AddEmployeeTransaction):
    def __init__(self, emp_id: int, address: str, name: str, salary: float):
        self._salary = salary
        super().__init__(emp_id, address, name)

    def _get_classification(self) -> SalariedClassification:
        return SalariedClassification(self._salary)

    def _get_schedule(self) -> PaymentSchedule:
        return PaymentSchedule()


class AddCommissionedEmployee(AddEmployeeTransaction):
    def __init__(
        self,
        emp_id: int,
        address: str,
        name: str,
        salary: float,
        commission_rate: float,
    ):
        self._salary = salary
        self._commission_rate = commission_rate
        super().__init__(emp_id, address, name)

    def _get_classification(self) -> CommissionedClassification:
        return CommissionedClassification(self._salary)

    def _get_schedule(self) -> PaymentSchedule:
        return PaymentSchedule()


class AddHourlyEmployee(AddEmployeeTransaction):
    def __init__(self, emp_id: int, address: str, name: str, hourly_rate: float):
        self._hourly_rate = hourly_rate
        super().__init__(emp_id, address, name)

    def _get_classification(self) -> HourlyClassification:
        return HourlyClassification()

    def _get_schedule(self) -> PaymentSchedule:
        return PaymentSchedule()


class DeleteEmployeeTransaction(Transaction):
    def __init__(self, emp_id: int):
        self._emp_id = emp_id

    def execute(self):
        GpayrollDatabase.delete_employee(self._emp_id)


class TimeCardTransaction(Transaction):
    def __init__(self, date: int, hourly: float, emp_id: int):
        self._date = date
        self._hourly = hourly
        self._emp_id = emp_id

    def execute(self):
        try:
            e = GpayrollDatabase.get_employee(self._emp_id)
        except KeyError:
            raise Exception("No such employee.")

        hc = e.classification
        if isinstance(hc, HourlyClassification):
            hc.add_time_card(TimeCard(date=self._date, hourly=self._hourly))
        else:
            raise Exception("Tried to add timecard to non-hourly employee")


class SalesReceiptTransaction(Transaction):
    def __init__(self, date: int, amount: float, emp_id: int):
        self._date = date
        self._amount = amount
        self._emp_id = emp_id

    def execute(self):
        try:
            e = GpayrollDatabase.get_employee(self._emp_id)
        except KeyError:
            raise Exception("No such employee.")

        cc = e.classification
        if isinstance(cc, CommissionedClassification):
            cc.add_sales_receipt(SalesReceipt(date=self._date, amount=self._amount))
        else:
            raise Exception("Tried to add sales receipt to non-amount employee")


class ServiceChargeTransaction(Transaction):
    def __init__(self, member_id: int, date: int, amount: float):
        self._member_id = member_id
        self._date = date
        self._amount = amount

    def execute(self):
        try:
            e = GpayrollDatabase.get_union_member(self._member_id)
        except KeyError:
            raise Exception("No such union_member.")

        uaf = e.affiliation
        if isinstance(uaf, UnionAffiliation):
            uaf.add_service_charge(ServiceCharge(date=self._date, amount=self._amount))
        else:
            raise Exception("Tried to add service charge to non-amount employee")
