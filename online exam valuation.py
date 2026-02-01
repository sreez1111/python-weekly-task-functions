def validate_answers(student_answers, correct_answers):
    return len(student_answers) == len(correct_answers)

def calculate_score(student_answers, correct_answers):
    score = 0
    for s, c in zip(student_answers, correct_answers):
        if s == c:
            score += 1
    return score

def generate_grade(score, total):
    percentage = (score / total) * 100
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"

# 🔽 FUNCTION CALLS
correct = ['A', 'B', 'C', 'D', 'A']
student = ['A', 'B', 'D', 'D', 'A']

if validate_answers(student, correct):
    score = calculate_score(student, correct)
    grade = generate_grade(score, len(correct))
    print("Score:", score)
    print("Grade:", grade)
else:
    print("Answer length mismatch")
