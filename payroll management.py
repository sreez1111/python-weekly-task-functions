def payroll(basic, bonus=0, deduction=0):
    return basic + bonus - deduction

salary = payroll(20000, bonus=3000, deduction=2000)
print("Net Salary:", salary)
