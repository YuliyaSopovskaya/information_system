


def get_value():
    value = str.capitalize(input())
    return value

def set_surname():
    print('фамилия - ')
    value = get_value()
    return value

def get_surname(emp):
    return emp[0]

def set_name():
    print('имя - ')
    value = get_value()
    return value

def get_name(emp):
    return emp[1]

def set_job_title():
    print('должность - ')
    value = get_value()
    return value

def get_job_title(emp):
    return emp[4]

def set_borndate():
    print('д.р.(dd/mm/yyyy) - ')
    value = get_value()
    return value

def get_borndate(emp):
    return emp[2]

def get_salary(emp):
    return emp[5]

def set_salary():
    print('зарплата ')
    value = get_value()
    return value

def get_rank(emp):
    return emp[4]

def set_rank():
    print('разряд ')
    rank = get_value()
    return rank