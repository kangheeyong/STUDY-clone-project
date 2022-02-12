from .database import PayrollDatabase
from .employee import AddSalariedEmployee


def test_add_salaried_employee():
    emp_id = 1

    emp = AddSalariedEmployee(emp_id, "Bob", "Home", 1000.0)
    emp.execute()

    e = PayrollDatabase.get_employee(emp_id)
    assert "Bob" == e.name

    pc = e.get_classification()
    assert pc

    assert 1000.0 == pc.salary

    ps = e.get_schedule()
    assert ps
