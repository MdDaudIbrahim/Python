"""
=============================================================================
                PRACTICE PROBLEMS - CONDITIONAL STATEMENTS
=============================================================================

This file contains practice problems to help you understand 
conditional statements (if, elif, else) in Python.

=============================================================================
"""


# =============================================================================
# PROBLEM 1: Check Odd or Even
# =============================================================================
"""
Write a Python program to check whether a number entered by the user 
is odd or even, and print the result.
"""

print("=" * 50)
print("PROBLEM 1: Check Odd or Even")
print("=" * 50)

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

"""
Example Output 1:
-----------------
Enter a number: 10
Even

Example Output 2:
-----------------
Enter a number: 5
Odd
"""


# =============================================================================
# PROBLEM 2: Grade Students Based on Marks
# =============================================================================
"""
Write a Python program to grade students based on their marks using the
following criteria:
    - If marks are 90 or above, grade = "A"
    - If marks are 80 to 89, grade = "B"
    - If marks are 70 to 79, grade = "C"
    - If marks are below 70, grade = "D"
Then print the grade.
"""

print("\n" + "=" * 50)
print("PROBLEM 2: Grade Students Based on Marks")
print("=" * 50)

marks = int(input("Enter student's marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "D"

print("Grade:", grade)

"""
Example Output:
---------------
Enter student's marks: 73
Grade: C
"""


# =============================================================================
# PROBLEM 3: Find the Greatest of Three Numbers
# =============================================================================
"""
Write a Python program to input three numbers from the user and print 
the greatest among them.
"""

print("\n" + "=" * 50)
print("PROBLEM 3: Find the Greatest of Three Numbers")
print("=" * 50)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    greatest = a
elif b >= a and b >= c:
    greatest = b
else:
    greatest = c

print("The greatest number is:", greatest)

"""
Example Output 1:
-----------------
Enter first number: 10
Enter second number: 20
Enter third number: 30
The greatest number is: 30

Example Output 2:
-----------------
Enter first number: 15
Enter second number: 10
Enter third number: 5
The greatest number is: 15

Example Output 3:
-----------------
Enter first number: 7
Enter second number: 21
Enter third number: 14
The greatest number is: 21
"""


# =============================================================================
# PROBLEM 4: Check Divisibility by 2, 5, and 11
# =============================================================================
"""
Write a Python program to check whether a number is divisible by 2, 5, and 11.
Also, demonstrate the use of both OR and AND operators in the program.
"""

print("\n" + "=" * 50)
print("PROBLEM 4: Check Divisibility (AND & OR Operators)")
print("=" * 50)

num = int(input("Enter a number: "))

# Using AND operator to check if divisible by 2, 5, and 11
if num % 2 == 0 and num % 5 == 0 and num % 11 == 0:
    print("Number is divisible by 2, 5, and 11.")
else:
    print("Number is NOT divisible by 2, 5, and 11.")

# Demonstrating OR operator (for learning)
if num % 2 == 0 or num % 5 == 0 or num % 11 == 0:
    print("Number is divisible by at least one of 2, 5, or 11.")
else:
    print("Number is not divisible by 2, 5, or 11.")

"""
Example Output 1:
-----------------
Enter a number: 110
Number is divisible by 2, 5, and 11.
Number is divisible by at least one of 2, 5, or 11.

Example Output 2:
-----------------
Enter a number: 37
Number is NOT divisible by 2, 5, and 11.
Number is not divisible by 2, 5, or 11.
"""


# =============================================================================
# BONUS PROBLEMS
# =============================================================================

print("\n" + "=" * 50)
print("BONUS PROBLEM 1: Check Positive, Negative, or Zero")
print("=" * 50)

"""
Write a program to check if a number is positive, negative, or zero.
"""

num = int(input("Enter a number: "))

if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")


print("\n" + "=" * 50)
print("BONUS PROBLEM 2: Check Leap Year")
print("=" * 50)

"""
Write a program to check if a year is a leap year.
A leap year is:
    - Divisible by 4
    - But not divisible by 100, unless also divisible by 400
"""

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is NOT a Leap Year")

"""
Example Output 1:
-----------------
Enter a year: 2024
2024 is a Leap Year

Example Output 2:
-----------------
Enter a year: 1900
1900 is NOT a Leap Year
"""


print("\n" + "=" * 50)
print("BONUS PROBLEM 3: Simple Calculator")
print("=" * 50)

"""
Write a simple calculator that takes two numbers and an operator,
then performs the operation.
"""

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operator!")

"""
Example Output:
---------------
Enter first number: 10
Enter operator (+, -, *, /): *
Enter second number: 5
Result: 10.0 * 5.0 = 50.0
"""
