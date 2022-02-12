class PaymentClassification:
    def __init__(self, salary: float):
        self._salary = salary

    @property
    def salary(self) -> float:
        return self._salary


class PaymentSchedule:
    pass


class PaymentMethod:
    pass
