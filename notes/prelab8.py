# Prelab 8

# 1. What is the output of the following code segment?
print("The output is False, True, False, False, True, False")
# 2. Given the list hours = [[5,4,10,4],[5,4],[7,4,3,8,4]] calculate the sum from each sublist and store each result in the list total_hours.

hours = [[5, 4, 10, 4], [5, 4], [7, 4, 3, 8, 4]]
total_hours = [sum(hours[0]), sum(hours[1]), + sum(hours[2])]

print(f"The sum of sublist 1 is {total_hours[0]}, the sum of sublist 2 is {total_hours[1]}, and the sum of sublist 3 is {total_hours[2]}.")

print(f"The total is {total_hours[0] + total_hours[1] + total_hours[2]}.")

# 3. Given the list hours = [[5,4,10,4],[5,4],[7,4,3,8,4]] print each individual value apart from being in the list.

hours = [[5, 4, 10, 4],[5, 4],[7, 4, 3, 8, 4]]

for numbers in hours:
    for num in numbers: 
        print(num)

# 4. Create a new list, hours2, from the list hours1 =[7,4,3,8,4] that is one less from each value. You must use list comprehension.
hours1 = [7, 4, 3, 8, 4]
hours2 = [i - 1 for i in hours1]
print(hours2)

# 5. Given the list hours = [[5,4,10,4],[5,4],[7,4,3,8,4]] add the number 3 between the 5 and 4 of the second number of hours
hours = [[5,4,10,4],[5,4],[7,4,3,8,4]]
hours[1].insert(1,3)
print(hours)

# 6. Give a tuple names with items "Alice", "Brian", "Chloe", "David", "Emma" (listed in this order), write a code segment that give a second tuple, names2, that consists of only the first 3 names. You must use the slicing technique.
names = ("Alice", "Brian", "Chloe", "David", "Emma")
names2 = names[0:3]
print(names2)