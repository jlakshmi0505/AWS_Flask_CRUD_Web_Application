import mock

from models import Employee, EmpSalary


def test_add_employee():
    mock_employee = mock.Mock(spec=Employee)
    mock_employee.add_employee.return_value = True
    actual = mock_employee.add_employee('b', 'b@gmail.com', 'USA', 'Google')
    assert actual


def test_update_employee():
    mock_employee = mock.Mock(spec=Employee)
    mock_employee.update_employee.return_value = True
    actual = mock_employee.update_employee(1, 'b1', 'b@gmail.com', 'USA-101', 'Facebook')
    assert actual


def test_delete_employee():
    mock_employee = mock.Mock(spec=Employee)
    mock_employee.delete_employee.return_value = True
    actual = mock_employee.delete_employee(1)
    assert actual


# ------------- Salary Unit test case ------------


def test_add_employee_salary():
    mock_employee_salary = mock.Mock(spec=EmpSalary)
    mock_employee_salary.add_employee_salary.return_value = True
    actual = mock_employee_salary.add_employee_salary(1, "100", "USD", "Deposit", "Biweekly")
    assert actual


def test_update_employee_salary():
    mock_employee_salary = mock.Mock(spec=EmpSalary)
    mock_employee_salary.update_employee_salary.return_value = True
    actual = mock_employee_salary.update_employee_salary(1, "500", "USD", "Deposit", "Biweekly")
    assert actual


def test_delete_employee_salary():
    mock_employee_salary = mock.Mock(spec=EmpSalary)
    mock_employee_salary.delete_employee_salary.return_value = True
    actual = mock_employee_salary.delete_employee_salary(1)
    assert actual

