# Lab Exercise 1: Grade Calculator

score = int(input("Test Score (0-100): "))
if 1 <= score <= 100:
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
    print(f"Test Grade: {grade}")
else:
    print("Error")