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
    filename = input("Please enter file name: ")
    bones = []
    
    with open(filename, "r") as file: # read the bones.dat file
        for line in file: 
            part = line.split()

            bone_type = part[0]
            name = part[1]
            length = float(part[2])
            outer_radius = float(part[3])
            inner_radius = float(part[4])
            moment = float(part[5])

            bone = Bone(name, length, outer_radius, inner_radius, moment, bone_type)
            bones.append(bone)
            
    for bone in bones:
        print("Bone Information: ")
        print("-" * 20)
        bone.display_info()
        print("_" * 20)
    

class Bone(): # class Bone

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
        I = self.calculate_moment_of_inertia()
        c = self.__outer_radius
        M = self.__moment
        step1 = (M * c) / I
        step2 = step1 / 1000000
        return step2

    def display_info(self): # display, calculate status

        if self.calculate_bending_stress() >= 170:
            status = "SAFE"
        else:
            status = "WARNING – RISK OF FRACTURE"

        print(f"Bone: {self.__bone_type} {self.__name}")
        print(f"Length: {self.__length:.3f} m")
        print(f"Outer Radius: {self.__outer_radius:.4f} m")
        print(f"Inner Radius: {self.__inner_radius:.4f} m")
        print(f"Moment: {self.__moment:.2f} N * m")
        print(f"Moment of Inertia: {self.calculate_moment_of_inertia():.2f} m^4")
        print(f"Bending Stress: {self.calculate_bending_stress()} MPa")
        print(f"Status: {status}")


if __name__ == "__main__":
    main()