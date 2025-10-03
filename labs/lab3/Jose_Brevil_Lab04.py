"""
    Name: Jose F. Brevil, Jr.
    Student ID: 011064137
    Submission Date: 10.03.25
    Program: Lab 4
    Sources Consulted: Runestone Academy - How to Think Like a Computer Scientist: Interactive Edition

    By submitting this work, I attest that it is my original work and that I did not violate
    the University of Mississippi academic policies set forth in the M book or any
    policies of the course.
"""

# Q1: Concrete Mixer Load Cycles

while True:
    try:
        num_rotations = float(input("Enter the number of rotations: "))
        if num_rotations.is_integer() and num_rotations > 0:
            break
        else:
            print("Please enter a valid number.")
    except ValueError:
        print("Please enter a valid number.")

while num_rotations < 0:
    try:
        num_rotations = int(input("Please enter a valid number of rotations (greater than 0): "))
    except ValueError:
        print("Please enter a valid number.")

num = 0

while num < num_rotations:
    print(f"Rotation {num+1} complete.")
    num += 1
print(f"Mixing finished after {num} rotations.")

print("\n"+ "="*50)

# Q2: Bridge Material Delivery

while True:
    try:
        total_req = int(input("Enter total tons required: "))
        if total_req > 0:
            break
        else:
            print("Please enter a valid number. (Greater than 0)")
    except ValueError:
        print("Please enter a valid number.")

delivery_num = []
delivered = 0

while delivered < total_req:
    try:
        tons = int(input("Enter tons to deliver: "))
        if tons <= 0:
            print("Please enter a valid number. (Greater than 0)")
            continue

        if delivered + tons > total_req:
            print(f"Invalid delivery. You can deliver up to {total_req - delivered} tons.")
        else:
            delivery_num.append(tons)
            delivered += tons
    except ValueError:
        print("Please enter a valid number.")

print(f"All {total_req} tons delivered in {len(delivery_num)} deliveries.")

print("\n"+ "="*50)

# Q3: Quality Control Testing (5 points)

strength = []

while True:
    try:
        user_input = int(input("Enter strength (-999 to stop): "))

        if user_input == -999:
            break
        elif user_input < 0:
            print("Invalid strength. Please enter a value of at least 0.")
            continue
        else:
            strength.append(user_input)
    except ValueError:
        print("Invalid strength. Please enter a valid number.")

from time import sleep

print("Calculating..." + "\n")

sleep(0.5)
if strength:
    avg_strength = sum(strength) / len(strength)
    strongest_strength = max(strength)
    print(f"Recorded strengths: {strength}")
    print(f"Average strength: {avg_strength:.1f} MPa")
    print(f"Strongest strength: {strongest_strength} MPa")

print("\n"+ "="*50)

# Q4: Password Checker
while True:
        password = input("Enter password: ")

# Criteria
        uppercase = False
        lowercase = False
        digits = False
        special = False
        proper_length = False
# Checker
        for ch in password:
            if ch.isupper():
                uppercase = True
            elif ch.islower():
                lowercase = True
            elif ch.isdigit():
                digits = True
            elif not ch.isalnum():
                special = True

        if len(password) >= 10:
            proper_length = True
# Score

        score = 0
        if uppercase:
            score += 1
        if lowercase:
            score += 1
        if digits:
            score += 1
        if special:
            score += 2
        if proper_length:
            score += 2


        if score <= 2:
            pw_strength = "Very Weak"
        elif score == 3:
            pw_strength = "Very Weak"
        elif score == 4:
            pw_strength = "Weak"
        elif score == 5:
            pw_strength = "Fair"
        elif score == 6:
            pw_strength = "Strong"
        elif score == 7:
            pw_strength = "Very Strong"


        if score >= 5 and special and proper_length:
            print(f"Password strength is {score} ({pw_strength})")
            print("Password accepted.")
            break
        else:
            print(f"Password strength is {score} ({pw_strength}) - must be at least Strong.")


