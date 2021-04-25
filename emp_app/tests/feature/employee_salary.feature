Feature: Employee salary CRUD Operation

    Want to test the Create, Update, Delete, Read functionality

    Scenario: Adding Employee Salary
    Given Employee and Employee Salary table is empty
    And Employee is created with "<employee_details>"
    When the Employee salary add API is queried with "<employee_salary_details>"
    Then the response status code is 200
    And the response shows the employee salary row id as "<row_id>"

    Examples: Employee
    |               employee_details             |             employee_salary_details            | row_id  |
    |   bob,bob@gmail.com,California-USA,Google  |      1,450000,dollar,saving_account,monthly    |    1    |


    Scenario: Update existing Employee salary
    Given Employee and Employee Salary table is empty
    And Employee is created with "<employee_details>"
    And add Employee Salary with "<employee_salary_details>"
    When the Employee salary update API is queried with "<employee_updated_salary_details>"
    Then the response status code is 200
    And the response shows the employee salary as "<new_salary>"

    Examples: Employee
    |               employee_details             |          employee_salary_details            |     employee_updated_salary_details        |  new_salary   | 
    |   bob,bob@gmail.com,California-USA,Google  |   1,450000,dollar,saving_account,monthly    |  1,550000,dollar,saving_account,monthly    |    550000     | 


    Scenario: Delete existing Employee salary
    Given Employee and Employee Salary table is empty
    And Employee is created with "<employee_details>"
    And add Employee Salary with "<employee_salary_details>"
    When the Employee salart delete API is queried with "<emp_id>"
    Then the response status code is 200
    

    Examples: Employee
    |               employee_details             |          employee_salary_details           | emp_id |  
    |   bob,bob@gmail.com,California-USA,Google  |  1,450000,dollar,saving_account,monthly    |   1    |