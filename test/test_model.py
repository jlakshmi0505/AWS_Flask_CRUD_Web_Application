import mock

from app import add_employee
from models import Employee, EmpSalary


def test_add_employee():
    mock_employee = mock.Mock(spec=Employee)
    actual = add_employee('b', 'b@gmail.com', 'USA', 'Google')
    mock_employee.save.assert_called()
    assert actual


def test_update_employee():
    mock_employee = mock.Mock(spec=Employee)
    actual = mock_employee.update_employee(1, 'b1', 'b@gmail.com', 'USA-101', 'Facebook')
    mock_employee.save.assert_called()
    assert actual


def test_delete_employee():
    mock_employee = mock.Mock(spec=Employee)
    actual = mock_employee.delete_employee(1)
    mock_employee.delete.assert_called()
    assert actual


# ------------- Salary Unit test case ------------


def test_add_employee_salary():
    mock_employee_salary = mock.Mock(spec=EmpSalary)
    actual = mock_employee_salary.add_employee_salary(1, "100", "USD", "Deposit", "Biweekly")
    mock_employee_salary.save.assert_called()

    assert actual


def test_update_employee_salary():
    mock_employee_salary = mock.Mock(spec=EmpSalary)
    actual = mock_employee_salary.update_employee_salary(1, "500", "USD", "Deposit", "Biweekly")
    mock_employee_salary.save.assert_called()
    assert actual


def test_delete_employee_salary():
    mock_employee_salary = mock.Mock(spec=EmpSalary)
    actual = mock_employee_salary.delete_employee_salary(1)
    mock_employee_salary.delete.assert_called()
    assert actual

