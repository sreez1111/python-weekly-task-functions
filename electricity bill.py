def calculate_bill(units):
    if units <= 100:
        return units * 1.5
    elif units <= 300:
        return 100*1.5 + (units-100)*2.5
    else:
        return 100*1.5 + 200*2.5 + (units-300)*4

units = int(input("Enter units consumed: "))
bill = calculate_bill(units)
print("Electricity Bill:", bill)
