def input_employee():
    name = input("Name: ")
    basic = float(input("Basic Salary: "))
    return name, basic

def gross_salary(basic):
    hra = 0.2 * basic
    da = 0.1 * basic
    return basic + hra + da

def deductions(gross):
    pf = 0.12 * gross
    return pf

def final_salary():
    name, basic = input_employee()
    gross = gross_salary(basic)
    ded = deductions(gross)
    final_salary_amount = gross - ded
    print(name, "final salary:", final_salary_amount)

final_salary()
