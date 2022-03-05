import pytest

from .database import GpayrollDatabase
from .employee import (
    AddCommissionedEmployee,
    AddHourlyEmployee,
    AddSalariedEmployee,
    CommissionedClassification,
    DeleteEmployeeTransaction,
    HourlyClassification,
    SalariedClassification,
    TimeCardTransaction,
)


def test_add_salaried_employee():
    emp_id = 1

    emp = AddSalariedEmployee(emp_id, "Bob", "Home", 1000.0)
    emp.execute()

    e = GpayrollDatabase.get_employee(emp_id)
    assert "Bob" == e.name

    sc = e.classification
    assert isinstance(sc, SalariedClassification)

    assert 1000.0 == sc.salary

    ps = e.schedule
    assert ps


def test_add_commissioned_employee():
    emp_id = 2

    emp = AddCommissionedEmployee(emp_id, "Bob", "Home", 1000.0, 1.2)
    emp.execute()

    e = GpayrollDatabase.get_employee(emp_id)
    assert "Bob" == e.name

    cc = e.classification
    assert isinstance(cc, CommissionedClassification)

    assert 1000.0 == cc.salary

    ps = e.schedule
    assert ps


def test_delete_employee():
    emp_id = 3

    emp = AddSalariedEmployee(emp_id, "Bob", "Home", 1000.0)
    emp.execute()

    e = GpayrollDatabase.get_employee(emp_id)
    assert e

    dt = DeleteEmployeeTransaction(emp_id)
    dt.execute()

    e = GpayrollDatabase.get_or_none_employee(emp_id)
    assert e is None


def test_time_card_transaction():

    emp_id = 4

    emp = AddHourlyEmployee(emp_id, "bill", "Home", 15.25)
    emp.execute()

    tct = TimeCardTransaction(20011031, 8.0, emp_id)
    tct.execute()

    e = GpayrollDatabase.get_or_none_employee(emp_id)
    assert e is not None

    hc = e.classification
    assert isinstance(hc, HourlyClassification)

    tc = hc.get_time_card(20011031)
    assert tc.hourly == 8.0


def test_raise_time_card_transaction():
    emp_id = -1

    tct = TimeCardTransaction(20011031, 8.0, emp_id)
    with pytest.raises(Exception):
        tct.execute()
