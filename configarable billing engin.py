def billing(amount, tax_func):
    return amount + tax_func(amount)

def gst(amount):
    return amount * 0.18

# 🔽 FUNCTION CALL
total = billing(1000, gst)
print("Final Amount:", total)
