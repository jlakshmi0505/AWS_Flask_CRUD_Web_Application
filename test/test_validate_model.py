from validate_model import ValidateModel


def test_validate_emp_name():
    actual = ValidateModel.validate_emp("jaya", "jaya.l@gmail.com", "ddd", "jhjhj")
    assert actual


def test_validate_emp_name_Invalid():
    actual = ValidateModel.validate_emp("", "jaya.l@gmail.com", "ddd", "jhjhj")
    assert not actual


def test_validate_emp_email():
    actual = ValidateModel.validate_emp("jaya", "jaya.l@gmail.com", "ddd", "jhjhj")
    assert actual


def test_validate_emp_email_Invalid():
    actual = ValidateModel.validate_emp("jaya", "m", "ddd", "jhjhj")
    assert not actual


def test_validate_emp_address():
    actual = ValidateModel.validate_emp("jaya", "jaya.l@gmail.com", "Hyderabad", "jhjhj")
    assert actual


def test_validate_emp_address_Invalid():
    actual = ValidateModel.validate_emp("jaya", "jaya.l@gmail.com", "", "jhjhj")
    assert not actual


def test_validate_emp_cmpy():
    actual = ValidateModel.validate_emp("jaya", "jaya.l@gmail.com", "Hyderabad", "Progress software")
    assert actual


def test_validate_emp_cmpy_Invalid():
    actual = ValidateModel.validate_emp("jaya", "jaya.l@gmail.com", "Hyderabad", "")
    assert not actual


# ------------- Salary Unit test case ------------

def test_validate_emp_salary_emp_id():
    actual = ValidateModel.validate_sal(1, 10000, "USD", "Deposit", "Biweekly")
    assert actual


def test_validate_emp_salary_emp_id_Invalid():
    actual = ValidateModel.validate_sal(-1, 10000, "USD", "Deposit", "Biweekly")
    assert not actual


def test_validate_emp_salary_sal():
    actual = ValidateModel.validate_sal(1, 10000, "USD", "Deposit", "Biweekly")
    assert actual


def test_validate_emp_salary_sal_Invalid():
    actual = ValidateModel.validate_sal(1, -10000, "USD", "Deposit", "Biweekly")
    assert not actual


def test_validate_emp_salary_currency():
    actual = ValidateModel.validate_sal(1, 10000, "USD", "Deposit", "Biweekly")
    assert actual


def test_validate_emp_salary_currency_Invalid():
    actual = ValidateModel.validate_sal(1, 10000, "", "Deposit", "Biweekly")
    assert not actual


def test_validate_emp_salary_pay_type():
    actual = ValidateModel.validate_sal(1, 10000, "USD", "Deposit", "Biweekly")
    assert actual


def test_validate_emp_salary_pay_type_Invalid():
    actual = ValidateModel.validate_sal(1, 10000, "USD", None, "Biweekly")
    assert not actual


def test_validate_emp_salary_pay_cycle():
    actual = ValidateModel.validate_sal(1, 10000, "USD", "Deposit", "Biweekly")
    assert actual


def test_validate_emp_salary_pay_cycle_Invalid():
    actual = ValidateModel.validate_sal(1, 10000, "USD", "Deposit", "")
    assert not actual
