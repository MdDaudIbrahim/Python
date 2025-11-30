"""
=============================================================================
                    PRACTICE PROBLEMS - INPUT
=============================================================================

This file contains practice problems to help you understand 
input() function and type conversion in Python.

=============================================================================
"""


# =============================================================================
# PROBLEM 1: Sum of Two Numbers
# =============================================================================
"""
Write a Program to input 2 numbers & print their sum.
"""

print("=" * 50)
print("PROBLEM 1: Sum of Two Numbers")
print("=" * 50)

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
sum = num1 + num2

print("Sum:", sum)

"""
Example Output:
---------------
Enter number 1: 10
Enter number 2: 20
Sum: 30
"""


# =============================================================================
# PROBLEM 2: Summation and Average of Five Numbers
# =============================================================================
"""
Write a Python program to take five float variables as input from the user.
Find out the summation and average of five numbers.
"""

print("\n" + "=" * 50)
print("PROBLEM 2: Summation and Average of Five Numbers")
print("=" * 50)

num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))
num4 = float(input("Enter number 4: "))
num5 = float(input("Enter number 5: "))

summ = num1 + num2 + num3 + num4 + num5
average = summ / 5

print("Summation:", summ)
print("Average:", average)

"""
Example Output:
---------------
Enter number 1: 10
Enter number 2: 3
Enter number 3: 7
Enter number 4: 6
Enter number 5: 8
Summation: 34.0
Average: 6.8
"""


# =============================================================================
# PROBLEM 3: Compute Z^5 + Z^7 + Z^9 + Z^4 - Z^3 * Z^2
# =============================================================================
"""
Write a python program that takes an integer variable, Z and computes the result
of Z^5 + Z^7 + Z^9 + Z^4 - Z^3 * Z^2. Do not use any built-in function.
"""

print("\n" + "=" * 50)
print("PROBLEM 3: Compute Z^5 + Z^7 + Z^9 + Z^4 - Z^3 * Z^2")
print("=" * 50)

z = int(input("Enter an integer number: "))

z2 = z * z       # Z^2
z3 = z2 * z      # Z^3
z4 = z2 * z2     # Z^4
z5 = z4 * z      # Z^5
z7 = z4 * z3     # Z^7
z9 = z5 * z4     # Z^9

result = z5 + z7 + z9 + z4 - (z3 * z2)

print("Z^5 + Z^7 + Z^9 + Z^4 - Z^3*Z^2 =", result)

"""
Example Output:
---------------
Enter an integer number: 4
Z^5 + Z^7 + Z^9 + Z^4 - Z^3*Z^2 = 278784
"""


# =============================================================================
# PROBLEM 4: Area of a Triangle
# =============================================================================
"""
Write a python program that has two variables, Base and Height and it computes
the area of a triangle.

Formula: Area = 0.5 * Base * Height
"""

print("\n" + "=" * 50)
print("PROBLEM 4: Area of a Triangle")
print("=" * 50)

a = float(input("Enter Base: "))
b = float(input("Enter Height: "))

area = 0.5 * a * b

print("Area is:", area)

"""
Example Output:
---------------
Enter Base: 5
Enter Height: 4
Area is: 10.0
"""


# =============================================================================
# PROBLEM 5: Compare Two Numbers
# =============================================================================
"""
Write a Python program to input two integer numbers, a and b. The program
should print True if a is greater than or equal to b. Otherwise, print False.
"""

print("\n" + "=" * 50)
print("PROBLEM 5: Compare Two Numbers")
print("=" * 50)

a = int(input("Enter the integer (a): "))
b = int(input("Enter the integer (b): "))

result = a >= b

print(result)

"""
Example Output 1:
-----------------
Enter the integer (a): 10
Enter the integer (b): 8
True

Example Output 2:
-----------------
Enter the integer (a): 10
Enter the integer (b): 20
False
"""


# =============================================================================
# PROBLEM 6: Area of a Square
# =============================================================================
"""
Write a python program that has one variable, Side and it computes 
the area of a square.

Formula: Area = Side * Side
"""

print("\n" + "=" * 50)
print("PROBLEM 6: Area of a Square")
print("=" * 50)

side = float(input("Enter side: "))
area = side * side

print("Area is:", area)

"""
Example Output:
---------------
Enter side: 5
Area is: 25.0
"""
