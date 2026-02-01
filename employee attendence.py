attendance = {}

def mark(name):
    attendance[name] = attendance.get(name, 0) + 1

def working_days(name):
    return attendance.get(name, 0)

def report():
    for k, v in attendance.items():
        print(k, v)

# 🔽 FUNCTION CALLS
mark("maya")
mark("anu")
mark("maya")

print("anu working days:", working_days("anu"))
print("maya working days:", working_days("maya"))

report()
