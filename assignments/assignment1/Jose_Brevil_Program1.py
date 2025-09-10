"""
    Name: Jose F. Brevil, Jr.
    Student ID: 011064137
    Submission Date: 09.08.25
    Program: Assignment 1
    Sources Consulted: Runestone Academy - How to Think Like a Computer Scientist: Interactive Edition, CIS 256 Week 3 Slides

    By submitting this work, I attest that it is my original work and that I did not violate
    the University of Mississippi academic policies set forth in the M book or any
    policies of the course.
"""

# Stress, Strain, Young's Modulus Calculator

import time

print("Welcome to the Stress, Strain, and Young's Modulus Calculator. \n Please enter any values in numerical form only, as inputting letters or special characters will cause an error.")
time.sleep(1)
print("Have fun!")
time.sleep(2)

# Input

material_name = input("Enter material name: ")
force = float(input("Enter force (e.g., '500 N'): "))
cross_area = float(input("Enter cross-sectional area (e.g., '0.01 m^2'): "))
org_length = float(input("Enter original length (e.g., '2 m'): "))
new_length = float(input("Enter new length (e.g., '2.005 m'): "))

print("***********")

# Processing

stress = force / cross_area
strain = (new_length - org_length) / org_length
young_modulus = float(stress) / float(strain)

# Output
print(f"Material: {material_name}")
print(f"Stress: {stress:.7} ")
print(f"Strain: {strain:.7}")
print(f"Young's Modulus: {young_modulus:,.10}")

