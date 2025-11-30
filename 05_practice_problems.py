"""
=============================================================================
                         PRACTICE PROBLEMS
=============================================================================

This file contains practice problems to help you understand variables 
and basic arithmetic operations in Python.

=============================================================================
"""


# =============================================================================
# PROBLEM 1: Addition
# =============================================================================
"""
Write a Python program that assigns values to variables num1, num2 
and performs addition operation. Also print the results.
"""

print("=" * 50)
print("PROBLEM 1: ADDITION")
print("=" * 50)

num1 = 10
num2 = 5
sum = num1 + num2

print("Sum:", sum)

# Output: Sum: 15


# =============================================================================
# PROBLEM 2: Subtraction
# =============================================================================
"""
Write a Python program that assigns values to variables num1, num2 
and performs subtraction operation. Also print the results.
"""

print("\n" + "=" * 50)
print("PROBLEM 2: SUBTRACTION")
print("=" * 50)

num1 = 10
num2 = 5
sub = num1 - num2

print("Sub:", sub)

# Output: Sub: 5


# =============================================================================
# PROBLEM 3: Multiplication & Division
# =============================================================================
"""
Write a Python program that assigns values to variables num1, num2 
and performs multiplication & division operations. Also print the results.
"""

print("\n" + "=" * 50)
print("PROBLEM 3: MULTIPLICATION & DIVISION")
print("=" * 50)

num1 = 10
num2 = 5
mult = num1 * num2
div = num1 / num2

print("Mult:", mult)
print("Div:", div)

# Output:
# Mult: 50
# Div: 2.0


# =============================================================================
# BONUS PROBLEMS
# =============================================================================

print("\n" + "=" * 50)
print("BONUS: ALL OPERATIONS TOGETHER")
print("=" * 50)

# Taking two numbers
a = 20
b = 7

# Performing all operations
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
floor_division = a // b     # Division without decimal
modulus = a % b             # Remainder
power = a ** b              # Exponentiation (a to the power b)

# Printing results
print(f"Numbers: a = {a}, b = {b}")
print(f"Addition (a + b): {addition}")
print(f"Subtraction (a - b): {subtraction}")
print(f"Multiplication (a * b): {multiplication}")
print(f"Division (a / b): {division}")
print(f"Floor Division (a // b): {floor_division}")
print(f"Modulus/Remainder (a % b): {modulus}")
print(f"Power (a ** b): {power}")

"""
Output:
-------
Numbers: a = 20, b = 7
Addition (a + b): 27
Subtraction (a - b): 13
Multiplication (a * b): 140
Division (a / b): 2.857142857142857
Floor Division (a // b): 2
Modulus/Remainder (a % b): 6
Power (a ** b): 1280000000
"""
