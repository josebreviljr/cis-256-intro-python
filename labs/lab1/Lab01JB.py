"""
    Name: Jose F. Brevil, Jr.
    Student ID: 011064137
    Submission Date: 08.29.25
    Program: Lab 1
    Sources Consulted: Runestone Academy - How to Think Like a Computer Scientist: Interactive Edition, CIS 256 Week 2 Slides

    By submitting this work, I attest that it is my original work and that I did not violate
    the University of Mississippi academic policies set forth in the M book or any
    policies of the course.
"""
# Q1: Type Casting, f-strings
qty_str, price_str, tax_rate_str = "42", "19.95", "0.074"

subtotal = int(qty_str) * float(price_str)
tax = float(subtotal) * float(tax_rate_str)
total = float(subtotal) + float(tax)

receipt_line = f"{qty_str} items @ {price_str} - subtotal {subtotal:.5}, tax {tax:.5}, total {round(total)}"
print(receipt_line)

print("********************")

# Q2: Basic Variable Assignment

title = "Starting Out with Python"
author = "Tony Gaddis"
year_published = 2024

print(f"{title} was written by {author} in {year_published}.")

print("********************")

# Q3: Swapping Variables

x,y = 10, 20
print(x, y)
something_i_like_to_call_memory = x
x, y = 20, something_i_like_to_call_memory
print(x, y)

# Q4: Data Type Identification

a, b, c, d = 5, 5.0, "5", True
print(type(a), type(b), type(c), type(d))

integer, floating, string, boolean = a, b, c, d
print(type(integer), type(floating), type(string), type(boolean))
print(integer, float, string, boolean)

# Q5: Arithmetic Operations
from math import pi

width = input("What width? ")
height = input("What height? ")
radius = input("What radius? ")

rect_perimeter = 2 * (int(width) * int(height))
print(f"The perimeter is {rect_perimeter}")

rect_area = (int(width) * int(height))
print(f"The area is {rect_area}")

circle_circumference = 2 * pi * int(radius)
print(f"The circumference is {circle_circumference:.4}")

circle_area = pi * (int(radius) ** 2)
print(f"The area is {circle_area:.4}")

print("********************")

# Q6: Grade Calculator

score1, score2, score3 = int(input("Score 1? ")), int(input("Score 2? ")), int(input("Score 3? ")) # Getting score input

avg_score = (score1 + score2 + score3) / 3

print(f"The average score is {avg_score}")

print("********************")

# Q7: GPA Conversion

gpa = (avg_score / 100) * 4
print(f"The GPA is {gpa}")


