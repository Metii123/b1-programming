# Lab Exercise 1: Grade Calculator

score = int(input("Test Score (0-100): "))
if 0 <= score <= 100:
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

# Lab Exercise 2: Limited Login Attempts:

correct_pin = 9876
attempts = 0
max_attempts = 3
login_succesful = False 

while attempts < max_attempts:
    print(f"Attempt {attempts + 1} of {max_attempts}")
    entered_pin = input("PIN: ")

    if entered_pin.isdigit():
        entered_pin = int(entered_pin)
        if entered_pin == correct_pin:
            print("Correct PIN!")
            login_succesful = True
            break
        else:
            print("Incorrect PIN!")
            attempts += 1
    else:
        print("Error: Wrong format, numbers only")

if not login_succesful:
    print("Too many incorrect attempts!")

# Lab Exercise 3: Filtering Even Numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in numbers:
    if i % 2 != 0:
        continue
    print(i)