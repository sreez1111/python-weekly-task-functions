# -------- Calculator Functions --------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# -------- String Functions --------
def string_length(s):
    return len(s)

def string_reverse(s):
    return s[::-1]

# -------- Number Utility Function --------
def is_even(n):
    return "Even" if n % 2 == 0 else "Odd"

# -------- Menu Function --------
def menu():
    print("\nMENU")
    print("1. Calculator")
    print("2. String Operations")
    print("3. Number Utilities")
    print("4. Exit")

# -------- Main Program --------
while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Addition:", add(a, b))
        print("Subtraction:", subtract(a, b))

    elif choice == "2":
        s = input("Enter a string: ")
        print("Length:", string_length(s))
        print("Reverse:", string_reverse(s))

    elif choice == "3":
        n = int(input("Enter a number: "))
        print("Result:", is_even(n))

    elif choice == "4":
        print("Program exited")
        break

    else:
        print("Invalid choice")
