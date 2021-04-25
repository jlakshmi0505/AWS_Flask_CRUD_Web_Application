import pytest
import request

from pytest_bdd import scenarios, when, then, given, And

CALLING_CODE_API = ""

scenarios('emp_app/tests/feature/employee_salaray.feature', example_converters= dict(employee_details=str, employee_salary_details =str,
employee_updated_salary_details = str, row_id = str, emp_id = str,
new_salary=str))


@pytest.fixture
@given('Employee and Employee Salary table is empty')



@when('the Employee salary add API is queried with "<employee_salary_details>"')
def create_employee_salary_response(employee_salary_details):
    return response


@when('the Employee delete API is queried with "<emp_id>"')
def delete_employee_response(emp_id):
    return response


@when('the Employee salary update API is queried with "<employee_updated_salary_details>"')
    def update_employee_salary_response(employee_updated_salary_details):
        return response

@then('the response status code is 200')
def response_code(create_employee_response):
    assert create_employee_response.status_code == 200


@And('the response shows the employee salary row id as "<row_id>"')
def check_response_row_id(emp_id):
    assert create_employee_response.row_id = row_id

@And('Employee is created with "<employee_details>"')
def create_employee(employee_details):
    return create_employee_response(employee_details)

@And('add Employee Salary with "<employee_salary_details>"')
def create_employee_salary(employee_salary_details):
    return response

@And('the response shows the employee salary as "<new_salary>"')
def employee_compay_check(new_salary):
    assert update_employee_salary_response.new_salary == new_salary


