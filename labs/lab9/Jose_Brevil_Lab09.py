"""
    Name: Jose F. Brevil, Jr.
    Student ID: 011064137
    Submission Date: 11.14.25
    Program: Lab 9
    Sources Consulted: Runestone Academy - How to Think Like a Computer Scientist: Interactive Edition

    By submitting this work, I attest that it is my original work and that I did not violate
    the University of Mississippi academic policies set forth in the M book or any
    policies of the course.
"""
from time import sleep

# Q1: Word Count 

print("—" * 20)
print("Q1: Word Count")
sleep(1)
sentence = input("Enter in a sentence: ").lower()

words = sentence.split()

word_counter = {}

for word in words:
    if word in word_counter:
        word_counter[word] += 1 
    else:
        word_counter[word] = 1

print("WORD COUNT")
for word, count in word_counter.items():
    print(f"\n{word} - {count}")


# Q2: Remove Zero-Value Entries 
print("—" * 20)
print("Q2: Remove Zero-Value Entries")
sleep(1)

message = {'This':4, 'Is':3, 'My':2, 'Message':1, 'But':0, 'Not':0, 'This one':0}

for key in list(message.keys()):
    if message[key] == 0:
        del message[key]

print(message)

# Q3: Car Colors 
print("—" * 20)
print("Q3: Car Colors")
sleep(1)

available_colors = {"cyan", "royal blue", "gray", "yellow"}
new_colors = {"black", "silver", "gold", "yellow"}

difference = new_colors - available_colors

all_colors = available_colors | new_colors
same_colors = available_colors & new_colors

print(f"Colors in new shipment not already in stock: {available_colors}")
print(f"Total available colors after shipment: {all_colors}")
print(f"Common colors between both sets: {same_colors}")

# Q4: Student Dictionary
print("—" * 20)
print("Q4: Student Dictionary")
sleep(1)

student = {"name": "Jose Brevil", "gpa": 4.8, "courses": {"PPL101": "A", "ISS125": "A"}}

def course_output(courses_dict): 
    for course, grade in courses_dict.items():
        print(f"Course: {course} – Grade: {grade}")

print(f"Student Name: {student['name']}")
print(f"GPA: {student['gpa']}")
print(f"Active courses:")
course_output(student['courses'])

new_course = input("Enter new course and grade separated by space: ")

course_name, grade = new_course.split()

student["courses"][course_name] = grade

course_output(student['courses'])

def update(student_dict, course_name, updated_grade):
    if course_name in student_dict["courses"]:
        student_dict['courses'][course_name] = updated_grade
    else:
        print(f"\nCourse {course_name} does not exist.")

course_update = input("Enter course to update and updated grade separated by space: ")
updated_course, updated_grade = course_update.split()

update(student, updated_course, updated_grade)

course_output(student['courses'])

print(student)

print("—" * 20)



