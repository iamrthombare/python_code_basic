# Problem: Grade a student based on score
# 90-100: A, 80-89: B, 70-79: C, 60-69: D, below 60: F

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")