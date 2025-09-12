"""
    Name: Jose F. Brevil, Jr.
    Student ID: 011064137
    Submission Date: 09.12.25
    Program: Lab 2
    Sources Consulted: Runestone Academy - How to Think Like a Computer Scientist: Interactive Edition

    By submitting this work, I attest that it is my original work and that I did not violate
    the University of Mississippi academic policies set forth in the M book or any
    policies of the course.
"""
# Q1: Student Grades

print("Question 1: Student Grades\n")

student_name = ["Alice", "Ben", "Clara", "David"]
student_major = ["Computer Science", "Math", "Biology", "History"]
student_gpa =  [3.7, 3.2, 3.9, 2.8]

output = "Student: {} \nMajor: {} \nGPA: {}".format(student_name[0], student_major[0], student_gpa[0])
output1 = "Student: {} \nMajor: {} \nGPA: {}".format(student_name[1], student_major[1], student_gpa[1])
output2 = "Student: {} \nMajor: {} \nGPA: {}".format(student_name[2], student_major[2], student_gpa[2])


print(f"{output} \n----------- \n{output1} \n----------- \n{output2} \n-----------")

# Q2: Arithmetic on Lists

print("Question 2: Arithmetic on Lists\n")

product_names = ["Apples", "Bananas", "Carrots", "Donuts"]
unit_price = [0.5, 0.3, 0.8, 1.2]
quantity_sold = [120, 200, 123, 75]

apple_sales = unit_price[0] * quantity_sold[0]
banana_sales = unit_price[1] * quantity_sold[1]
carrot_sales = unit_price[2] * quantity_sold[2]
donut_sales = unit_price[3] * quantity_sold[3]

sales = [apple_sales, banana_sales, carrot_sales, donut_sales]

data_output = "{}: {} X ${:.2f} = ${:.2f}".format(product_names[0], quantity_sold[0], unit_price[0], sales[0])
data_output1 = "{}: {} X ${:.2f} = ${:.2f}".format(product_names[1], quantity_sold[1], unit_price[1], sales[1])
data_output2 = "{}: {} X ${:.2f} = ${:.2f}".format(product_names[2], quantity_sold[2], unit_price[2], sales[2])
data_output3 = "{}: {} X ${:.2f} = ${:.2f}".format(product_names[3], quantity_sold[3], unit_price[3], sales[3])

print(f"{data_output} \n{data_output1} \n{data_output2} \n{data_output3}")
print("-----------")

# Q3: Tabular Data Formatting

print("Question 3: Tabular Data Formatting\n")

flight_number = ["AA101", "DL202", "UA203", "SW404"]
destination = ["New York", "Atlanta", "Chicago", "Dallas"]
ticket_price = [320, 250, 280, 200]

print(f"Flight Information: \n----------------------------------------"
      "\nFlight\t" "Destination\t" "\t \tTicket Price\t"
      "\n----------------------------------------")
for i in range(len(flight_number)):
    print("{:<10} {:<15} \t\t${:.2f}".format(flight_number[i], destination[i], ticket_price[i]))

