from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app

app = Flask(__name__)
app.secret_key = "Secret Key"   # need to access the session for flask application
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to avoid console warning

# Init DB
db = SQLAlchemy(app)

# Init MA
ma = Marshmallow(app)


# ---------------------------------- Employee REST Code ----------------------------
# Employee Class/Model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(200), unique=True)
    addr = db.Column(db.String(200))
    cmpy = db.Column(db.String(200))


    def __init__(self, name, email, addr, cmpy):
        self.name = name
        self.email = email
        self.addr = addr
        self.cmpy = cmpy


# Employee Schema
class EmployeeSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'email', 'addr', 'cmpy')

# Init schema
employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)

# Create a Employee
@app.route('/employee/add', methods=['POST'])
def add_employee():
    name = request.form['name']
    email = request.form['email']
    addr = request.form['addr']
    cmpy = request.form['cmpy']

    new_employee = Employee(name, email, addr, cmpy)

    db.session.add(new_employee)
    db.session.commit()

    flash("Employee added successfully!!")

    return redirect(url_for('Index'))


# Get All Employee
@app.route('/employees', methods=['GET'])
def get_employees():
  all_employees = Employee.query.all()
  return render_template("index.html", employees = all_employees)

# Get Single Employee
@app.route('/employee/getbyid/<id>', methods=['GET'])
def get_employee(id):
  employee = Employee.query.get(id)
  return employee_schema.jsonify(employee)

# Update a Employee
@app.route('/employee/update', methods=['POST'])
def update_employee():

  employee = Employee.query.get(request.form.get('id'))

  name = request.form['name']
  email = request.form['email']
  addr = request.form['addr']
  cmpy = request.form['cmpy']

  employee.name = name
  employee.email = email
  employee.addr = addr
  employee.cmpy = cmpy

  db.session.commit()
  flash("Employee Updated Successfully!!")
  return redirect(url_for('Index'))

# Delete Employee
@app.route('/employee/delete/<id>/', methods=['GET','POST'])
def delete_employee(id):
  employee = Employee.query.get(id)
  db.session.delete(employee)
  db.session.commit()

  flash("Employee Deleted Successfully!!")
  return redirect(url_for('Index'))

# ---------------------------------- Employee Salary REST Code ----------------------------

# Employee  Salary Class/Model
class EmpSalary(db.Model):
    __tablename__ = "EmpSalary"
    id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.Integer, unique=True)
    salary = db.Column(db.Float)
    currency = db.Column(db.String(200))
    pay_type = db.Column(db.String(200))
    pay_cycle = db.Column(db.String(200))


    def __init__(self, emp_id, salary, currency, pay_type, pay_cycle):
        self.emp_id = emp_id
        self.salary = salary
        self.currency = currency
        self.pay_type = pay_type
        self.pay_cycle = pay_cycle


# Employee Salary Schema
class EmpSalarySchema(ma.Schema):
  class Meta:
    fields = ('emp_id', 'salary', 'currency', 'pay_type', 'pay_cycle')

# Init schema
empsalary_schema = EmpSalarySchema()
empsalaries_schema = EmpSalarySchema(many=True)


# Create a Employee Salary
@app.route('/employee/salary/add', methods=['POST'])
def add_emp_salary():
    emp_id = request.form['emp_id']
    salary = request.form['salary']
    currency = request.form['currency']
    pay_type = request.form['pay_type']
    pay_cycle = request.form['pay_cycle']

    new_emp_sal = EmpSalary(emp_id, salary, currency, pay_type, pay_cycle )

    db.session.add(new_emp_sal)
    db.session.commit()

    flash("Employee Salary added successfully!!")

    return redirect(url_for('Index'))

# Get All Employee Salaries
@app.route('/employees/salaries', methods=['GET'])
def get_emp_salaries():
  all_emp_salaries = EmpSalary.query.all()
  return render_template("index.html", employees_salary = all_emp_salaries)

# Get Single Employee Salary
@app.route('/employee/salary/getbyid/<emp_id>', methods=['GET'])
def get_emp_salary(emp_id):
  employee = EmpSalary.query.get(emp_id)
  return empsalary_schema.jsonify(employee)

# Update a Employee Salary
@app.route('/employee/salary/update', methods=['POST'])
def update_emp_salary():
  employee = EmpSalary.query.get(request.form.get('emp_id'))

  salary = request.form['salary']
  currency = request.form['currency']
  pay_type = request.form['pay_type']
  pay_cycle = request.form['pay_cycle']

  employee.salary = salary
  employee.currency = currency
  employee.pay_type = pay_type
  employee.pay_cycle = pay_cycle

  db.session.commit()

  flash("Employee Salary Updated Successfully!!")
  return redirect(url_for('Index'))

# Delete Employee Salary
@app.route('/employee/salary/delete/<emp_id>', methods=['GET', 'POST'])
def delete_emp_salary(emp_id):
  employee = EmpSalary.query.filter_by(emp_id = emp_id).first()
  db.session.delete(employee)
  db.session.commit()

  flash("Employee Salary Deleted Successfully!!")
  return redirect(url_for('Index'))


@app.route('/')
def Index():

    all_employees = Employee.query.all()
    all_employees_salaries = EmpSalary.query.all()
    return render_template("index.html", employees = all_employees, employees_salary = all_employees_salaries)

# Run Server

if __name__ == '__main__':
    app.run(debug=True)


