def sales_report():
    print("Sales Report Generated")

def employee_report():
    print("Employee Report Generated")

def finance_report():
    print("Finance Report Generated")

def generate_report(report_function):
    report_function()

# 🔽 FUNCTION CALLS
generate_report(sales_report)
generate_report(employee_report)
generate_report(finance_report)
