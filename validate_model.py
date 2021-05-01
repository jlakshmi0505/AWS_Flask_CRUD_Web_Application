import re


class ValidateModel:
    def validate_emp(emp_name, email, addr, cmpy):
        regex_email = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if emp_name is None or not emp_name:
            return False
        elif not re.search(regex_email, email):
            return False
        elif addr is None or not addr:
            return False
        elif cmpy is None or not cmpy:
            return False
        return True

    def validate_sal(emp_id, salary, currency, pay_type, pay_cycle):
        if emp_id is None or not emp_id or int(emp_id) < 0:
            return False
        elif salary is None or not salary or int(salary) < 0:
            return False
        elif currency is None or not currency:
            return False
        elif pay_type is None or not pay_type:
            return False
        elif pay_cycle is None or not pay_cycle:
            return False
        return True
