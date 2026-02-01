cart = {}

def add_item(item, price):
    cart[item] = price

def remove_item(item):
    cart.pop(item, None)

def total_bill():
    return sum(cart.values())

def apply_discount(percent):
    return total_bill() * (1 - percent / 100)

# 🔽 FUNCTION CALLS
add_item("Book", 500)
add_item("Pen", 100)
add_item("Bag", 900)

print("Total:", total_bill())
print("After Discount:", apply_discount(10))
