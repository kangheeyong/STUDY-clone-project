from .database import GpayrollDatabase
from .employee import (
    AddCommissionedEmployee,
    AddSalariedEmployee,
    DeleteEmployeeTransaction,
)


def test_add_salaried_employee():
    emp_id = 1

    emp = AddSalariedEmployee(emp_id, "Bob", "Home", 1000.0)
    emp.execute()

    e = GpayrollDatabase.get_employee(emp_id)
    assert "Bob" == e.name

    pc = e.get_classification()
    assert pc

    assert 1000.0 == pc.salary

    ps = e.get_schedule()
    assert ps


def test_add_commissioned_employee():
    emp_id = 1

    emp = AddCommissionedEmployee(emp_id, "Bob", "Home", 1000.0, 1.2)
    emp.execute()

    e = GpayrollDatabase.get_employee(emp_id)
    assert "Bob" == e.name

    pc = e.get_classification()
    assert pc

    assert 1000.0 == pc.salary

    ps = e.get_schedule()
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
