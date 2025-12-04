"""
    Name: Jose F. Brevil, Jr.
    Student ID: 011064137
    Submission Date: 12.05.25
    Program: Assignment 5
    Sources Consulted: Runestone Academy - How to Think Like a Computer Scientist: Interactive Edition, CIS 256 Slides

    By submitting this work, I attest that it is my original work and that I did not violate
    the University of Mississippi academic policies set forth in the M book or any
    policies of the course.
"""
import math

def main():
    print("Welcome to the Bone Stress Calculator.")



class Bone():

    def __init__(self, name, length, outer_radius, inner_radius, moment, bone_type): 
       self.__name = name
       self.__length = length
       self.__outer_radius = outer_radius
       self.__inner_radius = inner_radius
       self.__moment = moment
       self.__bone_type = bone_type

    def calculate_moment_of_inertia(self):
        ro = self.__inner_radius 
        ri = self.__outer_radius
        inertia = (math.pi / 4) * (ro ** 4 - ri ** 4)
        return inertia



    def calculate_bending_stress(self):
        print("yes")

    def display_info(self):
        print("Yes")


if __name__ == "__main__":
    main()