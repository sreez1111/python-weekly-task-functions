def input_marks():
    marks = []
    for i in range(5):
        marks.append(int(input("Enter mark: ")))
    return marks

def calculate(marks):
    total = sum(marks)
    avg = total / len(marks)
    return total, avg

def grade(avg):
    if avg >= 90: return "A"
    elif avg >= 75: return "B"
    elif avg >= 50: return "C"
    else: return "Fail"

def display():
    m = input_marks()
    total, avg = calculate(m)
    print("Total:", total, "Grade:", grade(avg))
display()