"""
=============================================================================
                    PRACTICE PROBLEMS - FUNCTIONS
=============================================================================

This file contains practice problems to help you understand 
functions in Python.

=============================================================================
"""


# =============================================================================
# PROBLEM 1: Print List Length
# =============================================================================
"""
Write a function in Python that takes a list as a parameter 
and prints its length.
"""

print("=" * 50)
print("PROBLEM 1: Print List Length")
print("=" * 50)

def print_list_length(lst):
    print("Length of the list:", len(lst))

my_list = [10, 20, 30, 40]
print(f"List: {my_list}")
print_list_length(my_list)

"""
Output:
-------
List: [10, 20, 30, 40]
Length of the list: 4
"""


# =============================================================================
# PROBLEM 2: Print List Elements in Single Line
# =============================================================================
"""
Write a function that takes a list as a parameter and prints all its 
elements in a single line.
"""

print("\n" + "=" * 50)
print("PROBLEM 2: Print List Elements in Single Line")
print("=" * 50)

def print_elements_single_line(lst):
    for item in lst:
        print(item, end=' ')
    print()  # New line at end

my_list = [1, 2, 3, 4, 5]
print(f"List: {my_list}")
print("Elements:", end=' ')
print_elements_single_line(my_list)

"""
Output:
-------
List: [1, 2, 3, 4, 5]
Elements: 1 2 3 4 5
"""


# =============================================================================
# PROBLEM 3: Print Factorial
# =============================================================================
"""
Write a function in Python that takes a number n as a parameter 
and prints its factorial.

Factorial of 5 = 5 × 4 × 3 × 2 × 1 = 120
"""

print("\n" + "=" * 50)
print("PROBLEM 3: Print Factorial")
print("=" * 50)

def print_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print("Factorial of", n, "is", factorial)

num = int(input("Enter a Number: "))
print_factorial(num)

"""
Example Output:
---------------
Enter a Number: 5
Factorial of 5 is 120
"""


# =============================================================================
# PROBLEM 4: USD to BDT Converter
# =============================================================================
"""
Write a function in Python that takes an amount in USD and converts 
it to BDT. Assume 1 USD = 117 BDT.
"""

print("\n" + "=" * 50)
print("PROBLEM 4: USD to BDT Converter")
print("=" * 50)

def convert_usd_to_bdt(usd):
    bdt = usd * 117
    print(f"{usd} USD = {bdt} BDT")

amount = int(input("Enter Amount in USD: "))
convert_usd_to_bdt(amount)

"""
Example Output:
---------------
Enter Amount in USD: 50
50 USD = 5850 BDT
"""


# =============================================================================
# BONUS PROBLEMS
# =============================================================================

print("\n" + "=" * 50)
print("BONUS PROBLEM 1: Check Prime Number")
print("=" * 50)

"""
Write a function to check if a number is prime.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a Prime number")
else:
    print(f"{num} is NOT a Prime number")


print("\n" + "=" * 50)
print("BONUS PROBLEM 2: Calculate Average")
print("=" * 50)

"""
Write a function that takes a list of numbers and returns the average.
"""

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

grades = [85, 90, 78, 92, 88]
print(f"Grades: {grades}")
print(f"Average: {calculate_average(grades):.2f}")


print("\n" + "=" * 50)
print("BONUS PROBLEM 3: Fibonacci Sequence")
print("=" * 50)

"""
Write a function to generate Fibonacci sequence up to n terms.
"""

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

n = int(input("Enter number of Fibonacci terms: "))
print(f"Fibonacci sequence: {fibonacci(n)}")


print("\n" + "=" * 50)
print("BONUS PROBLEM 4: Temperature Converter")
print("=" * 50)

"""
Write functions to convert between Celsius and Fahrenheit.
"""

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

c = 37
f = 98.6

print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")
print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")


print("\n" + "=" * 50)
print("BONUS PROBLEM 5: Find Maximum in List (Without max())")
print("=" * 50)

"""
Write a function to find the maximum value in a list without using max().
"""

def find_max(lst):
    if len(lst) == 0:
        return None
    maximum = lst[0]
    for num in lst:
        if num > maximum:
            maximum = num
    return maximum

numbers = [45, 22, 89, 12, 67, 90, 34]
print(f"List: {numbers}")
print(f"Maximum: {find_max(numbers)}")
