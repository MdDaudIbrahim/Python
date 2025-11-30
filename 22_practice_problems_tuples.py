"""
=============================================================================
                    PRACTICE PROBLEMS - TUPLES
=============================================================================

This file contains practice problems to help you understand 
tuples and tuple operations in Python.

=============================================================================
"""


# =============================================================================
# PROBLEM 1: Count 'A' Grades
# =============================================================================
"""
Write a Python program to count how many students received an "A" grade 
in the following tuple: ("C", "D", "A", "A", "B", "B", "A")
"""

print("=" * 50)
print("PROBLEM 1: Count 'A' Grades")
print("=" * 50)

grades = ("C", "D", "A", "A", "B", "B", "A")

count_A = grades.count("A")
print(f"Grades: {grades}")
print("Number of 'A' grades:", count_A)

"""
Output:
-------
Grades: ('C', 'D', 'A', 'A', 'B', 'B', 'A')
Number of 'A' grades: 3
"""


# =============================================================================
# PROBLEM 2: Max and Min from User Input
# =============================================================================
"""
Write a Python program to input 5 numbers from the user, store them in 
a tuple, and then print the maximum and minimum values.
"""

print("\n" + "=" * 50)
print("PROBLEM 2: Max and Min from User Input")
print("=" * 50)

numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

number_tuple = tuple(numbers)

print("Tuple:", number_tuple)
print("Maximum value:", max(number_tuple))
print("Minimum value:", min(number_tuple))

"""
Example Output:
---------------
Enter a number: 10
Enter a number: 20
Enter a number: 30
Enter a number: 40
Enter a number: 50
Tuple: (10, 20, 30, 40, 50)
Maximum value: 50
Minimum value: 10
"""


# =============================================================================
# PROBLEM 3: Mixed Data Types in Tuple
# =============================================================================
"""
Create a tuple with mixed data types (e.g., ("Mohsin", 21, "CSE")) 
and print each item along with its data type.
"""

print("\n" + "=" * 50)
print("PROBLEM 3: Mixed Data Types in Tuple")
print("=" * 50)

info = ("Mohsin", 21, "CSE")

print(f"Tuple: {info}")
print("\nItems and their types:")
for item in info:
    print(f"  {item} => {type(item)}")

"""
Output:
-------
Tuple: ('Mohsin', 21, 'CSE')

Items and their types:
  Mohsin => <class 'str'>
  21 => <class 'int'>
  CSE => <class 'str'>
"""


# =============================================================================
# BONUS PROBLEMS
# =============================================================================

print("\n" + "=" * 50)
print("BONUS PROBLEM 1: Tuple Concatenation")
print("=" * 50)

"""
Create two tuples and concatenate them.
"""

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

combined = tuple1 + tuple2
print(f"tuple1 = {tuple1}")
print(f"tuple2 = {tuple2}")
print(f"Combined = {combined}")

# Output: (1, 2, 3, 4, 5, 6)


print("\n" + "=" * 50)
print("BONUS PROBLEM 2: Find Index of Item")
print("=" * 50)

"""
Find the index of a specific item in a tuple.
"""

fruits = ("apple", "banana", "cherry", "date")
item_to_find = input("Enter fruit to find: ")

if item_to_find in fruits:
    index = fruits.index(item_to_find)
    print(f"'{item_to_find}' is at index {index}")
else:
    print(f"'{item_to_find}' not found in tuple")


print("\n" + "=" * 50)
print("BONUS PROBLEM 3: Sum and Average of Tuple")
print("=" * 50)

"""
Calculate the sum and average of numbers in a tuple.
"""

numbers = []
n = int(input("How many numbers? "))

for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

number_tuple = tuple(numbers)

total = sum(number_tuple)
average = total / len(number_tuple)

print(f"\nTuple: {number_tuple}")
print(f"Sum: {total}")
print(f"Average: {average:.2f}")


print("\n" + "=" * 50)
print("BONUS PROBLEM 4: Tuple Unpacking")
print("=" * 50)

"""
Demonstrate tuple unpacking with student info.
"""

student = ("Alice", 20, "Computer Science", 3.8)

name, age, major, gpa = student

print(f"Student Tuple: {student}")
print(f"\nUnpacked values:")
print(f"  Name: {name}")
print(f"  Age: {age}")
print(f"  Major: {major}")
print(f"  GPA: {gpa}")
