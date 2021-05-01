from emp_app import db
from validate_model import ValidateModel


class BaseModel(db.Model):  # type: ignore # silences a mypy warning

    """
    Base model that all models inherit.

    Has common attributes and methods to all data models.

    """
    __abstract__ = True

    def save(self, commit=True):
        """Persists a new model in database."""
        db.session.add(self)
        if commit:
            try:
                db.session.commit()
            except Exception as save_exception:
                db.session.rollback()
                raise save_exception

    def delete(self, commit=True):
        """Removes model from database."""
        db.session.delete(self)
        if commit:
            db.session.commit()


class Employee(BaseModel):
    __tablename__ = "Employee"
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

    @staticmethod
    def exists(id):
        """Returns true if the provided Emp ID exists"""
        return Employee.query.filter_by(id=id).first()

    @staticmethod
    def get_all_employees():
        """Returns all the employees """
        return Employee.query.all()

    @staticmethod
    def add_employee(name, email, addr, cmpy):
        """Add a new Employee type """
        if ValidateModel.validate_emp(name, email, addr, cmpy):
            employee = Employee(name=name, email=email, addr=addr, cmpy=cmpy)
            employee.save()
            return True

    @staticmethod
    def update_employee(id, name, email, addr, cmpy):
        """Update employee """
        employee = Employee.exists(id)
        employee.name = name
        employee.email = email
        employee.addr = addr
        employee.cmpy = cmpy
        employee.save()
        return True

    @staticmethod
    def delete_employee(id):
        """Delete employee """
        employee = Employee.exists(id)
        employee.delete()
        return True

    @staticmethod
    def delete_all_records():
        """Delete records """
        emp_records = Employee.get_all_employees()
        for emp_rec in emp_records:
            emp_rec.delete()
        return True

    def validate_emp_params(name, email, addr, cmpy):
        if name is not None:
            return True


# Employee  Salary Class/Model
class EmpSalary(BaseModel):
    __tablename__ = "EmpSalary"
    id = db.Column(db.Integer, primary_key=True)
    emp_id = db.Column(db.Integer, db.ForeignKey("Employee.id"), nullable=False)
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

    @staticmethod
    def exists(id):
        """Returns true if the provided Emp ID exists"""
        return EmpSalary.query.filter_by(emp_id=id).first()

    @staticmethod
    def get_all_employees_salaries():
        """Returns all the employees salaries"""
        return EmpSalary.query.all()

    @staticmethod
    def add_employee_salary(emp_id, salary, currency, pay_type, pay_cycle):
        """Add a new Employee salary """
        if ValidateModel.validate_sal(emp_id, salary, currency, pay_type, pay_cycle):
            employee_salary = EmpSalary(emp_id, salary, currency, pay_type, pay_cycle)
            employee_salary.save()
            return True

    @staticmethod
    def update_employee_salary(emp_id, salary, currency, pay_type, pay_cycle):
        """Update employee """
        employee_salary = EmpSalary.exists(emp_id)
        employee_salary.salary = salary
        employee_salary.currency = currency
        employee_salary.pay_type = pay_type
        employee_salary.pay_cycle = pay_cycle
        employee_salary.save()
        return True

    @staticmethod
    def delete_employee_salary(id):
        """Delete employee salary """
        employee_salary = EmpSalary.exists(id)
        employee_salary.delete()
        return True

    @staticmethod
    def delete_all_salary_records():
        """Delete all salary records """
        emp_salary_records = EmpSalary.get_all_employees_salaries()
        for emp_salary_rec in emp_salary_records:
            emp_salary_rec.delete()
        return True
