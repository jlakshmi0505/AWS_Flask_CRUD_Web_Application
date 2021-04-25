Feature: Employee CRUD Operation

    Want to test the Create, Update, Delete, Read functionality

    Scenario: Adding New Employee
    Given Employee and Employee Salary table is empty
    When the Employee add API is queried with "<employee_details>"
    Then the response status code is 200
    And the response shows the employee id as "<emp_id>"

    Examples: Employee
    |               employee_details             |   emp_id  | 
    |   bob,bob@gmail.com,California-USA,Google  |      1    |


    Scenario: Update existing Employee
    Given Employee and Employee Salary table is empty
    And Employee is created with "<employee_details>"
    When the Employee update API is queried with "<employee_updated_details>"
    Then the response status code is 200
    And the response shows the employee company as "<emp_company>"

    Examples: Employee
    |               employee_details             |          employee_updated_details        |  emp_company | 
    |   bob,bob@gmail.com,California-USA,Google  |   bob,bob@gmail.com,California-USA,FB    |       FB     | 


    Scenario: Delete existing Employee
    Given Employee and Employee Salary table is empty
    And Employee is created with "<employee_details>"
    When the Employee delete API is queried with "<emp_id>"
    Then the response status code is 200
    

    Examples: Employee
    |               employee_details             |  emp_id |  
    |   bob,bob@gmail.com,California-USA,Google  |     1   |






    
         