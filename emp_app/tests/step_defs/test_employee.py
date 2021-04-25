import pytest
import request

from pytest_bdd import scenarios, when, then, given, And

CALLING_CODE_API = ""

scenarios('emp_app/tests/feature/employee.feature', example_converters= dict(employee_details=str, employee_updated_details =str,
emp_id = str, emp_company=str))


@pytest.fixture
@given('Employee and Employee Salary table is empty')



@when('the Employee add API is queried with "<employee_details>"')
def create_employee_response(employee_details):
    return response


@when('the Employee delete API is queried with "<emp_id>"')
def delete_employee_response(emp_id):
    return response


 @when('the Employee update API is queried with "<employee_updated_details>"')
 def update_employee_response(employee_updated_details):
     return response

@then('the response status code is 200')
def response_code(create_employee_response):
    assert create_employee_response.status_code == 200


@And('the response shows the employee id as "<emp_id>"')
def check_response_emp_id(emp_id):
    assert create_employee_response.emp_id = emp_id

@And('Employee is created with "<employee_details>"')
def create_employee(employee_details):
    return create_employee_response(employee_details)

@And('the response shows the employee company as "<emp_company>"')
def employee_compay_check(emp_company):
    assert update_employee_response.emp_cmpy == emp_company


