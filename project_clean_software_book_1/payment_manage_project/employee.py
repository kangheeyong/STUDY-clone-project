import abc

from .database import Employee, GpayrollDatabase
from .payment import PaymentClassification, PaymentMethod, PaymentSchedule


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
        empid: int,
        name: str,
        address: str,
    ):
        self._empid = empid
        self._name = name
        self._address = address

    def _get_classification(self) -> PaymentClassification:
        raise NotImplementedError()

    def _get_schedule(self) -> PaymentSchedule:
        raise NotImplementedError()

    def execute(self):
        e = Employee(
            _id=self._empid,
            name=self._name,
            address=self._address,
        )

        pc = self._get_classification()
        e.set_classification(pc)

        ps = self._get_schedule()
        e.set_schedule(ps)

        pm = PaymentMethod()
        e.set_method(pm)

        GpayrollDatabase.add_employee(self._empid, e)


class AddSalariedEmployee(AddEmployeeTransaction):
    def __init__(self, empid: int, address: str, name: str, salary: float):
        self._salary = salary
        super().__init__(empid, address, name)

    def _get_classification(self) -> PaymentClassification:
        return PaymentClassification(self._salary)

    def _get_schedule(self) -> PaymentSchedule:
        return PaymentSchedule()


class AddCommissionedEmployee(AddEmployeeTransaction):
    def __init__(
        self, empid: int, address: str, name: str, salary: float, commission_rate: float
    ):
        self._salary = salary
        self._commission_rate = commission_rate
        super().__init__(empid, address, name)

    def _get_classification(self) -> PaymentClassification:
        return PaymentClassification(self._salary)

    def _get_schedule(self) -> PaymentSchedule:
        return PaymentSchedule()


class DeleteEmployeeTransaction(Transaction):
    def __init__(self, empid: int):
        self._empid = empid

    def execute(self):
        GpayrollDatabase.delete_employee(self._empid)
