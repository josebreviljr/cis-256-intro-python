"""
    Name: Jose F. Brevil, Jr.
    Student ID: 011064137
    Submission Date: 10.03.25
    Program: Assignment 2
    Sources Consulted: Runestone Academy - How to Think Like a Computer Scientist: Interactive Edition, CIS 256 Slides

    By submitting this work, I attest that it is my original work and that I did not violate
    the University of Mississippi academic policies set forth in the M book or any
    policies of the course.
"""
# Nutrition Tracker – Daily Calorie Calculator

from time import sleep
# Intro
print("Welcome to the Nutrition Tracker!")
sleep(.5)
print("Please enter your meal(s) and their corresponding caloric value(s).")
sleep(.5)

# Meal count
while True:
    try:
        num_meals = int(input("How many meals have you had today? "))
        if num_meals > 0:
            break
        else:
            print("Please enter a valid number.")
    except ValueError:
        print("Please enter a valid number.")

meals = []
meal_total = []
daily_total = 0

print("Thank you.")
sleep(.5)

for i in range(num_meals):
        meal_name = (input(f"What was meal {i+1}? "))
        meals.append(meal_name)

        while True:
            try:
                calories = int(input(f"How many calories were in {meal_name}? "))
                if calories > 0:
                    break
                else:
                    print("Please enter a valid number.")
            except ValueError:
                print("Please enter a valid number.")
        meal_total.append(calories)
        daily_total += calories

if daily_total < 2000:
    message = "Below recommended intake. (Less than 2000 calories/day)"
elif daily_total <= 2500:
    message = "Within healthy range. (Greater than or equal to 2500 calories/day)"
else:
    message = "Greater than recommended intake. (Above 2500 calories/day)"

print("Thank you.")
sleep(1)
print("Calculating...")
sleep(1)

# Final Output

print("\n" + "="*50)
for i in range(len(meals)):
    print(f"{meals[i]}: {meal_total[i]} cal")
print("="*50)
print(f"TOTAL for the day: {daily_total} calories")
print(f"Health message: {message}")
print("="*50)

print("Thank you for using the Nutrition Tracker!")





