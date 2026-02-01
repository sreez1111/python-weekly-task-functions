balance = 0

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
    else:
        print("Insufficient balance")

def check_balance():
    print("Balance:", balance)

deposit(1000)     # add money
withdraw(300)     # remove money
check_balance()   # show balance
