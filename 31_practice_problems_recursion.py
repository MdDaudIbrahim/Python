"""
=============================================================================
                    PRACTICE PROBLEMS - RECURSION
=============================================================================

This file contains practice problems to help you understand 
recursion in Python.

=============================================================================
"""


# =============================================================================
# PROBLEM 1: Sum of First N Natural Numbers
# =============================================================================
"""
Write a recursive function to calculate the sum of the first n natural numbers.
Sum = 1 + 2 + 3 + ... + n
"""

print("=" * 50)
print("PROBLEM 1: Sum of First N Natural Numbers")
print("=" * 50)

def sum_natural(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural(n - 1)

num = int(input("Enter a Number: "))
print("Sum:", sum_natural(num))

"""
Example Output:
---------------
Enter a Number: 5
Sum: 15
"""


# =============================================================================
# BONUS PROBLEMS
# =============================================================================

print("\n" + "=" * 50)
print("BONUS PROBLEM 1: Count Digits")
print("=" * 50)

"""
Write a recursive function to count the number of digits in a number.
"""

def count_digits(n):
    n = abs(n)  # Handle negative numbers
    if n < 10:
        return 1                        # Base case: single digit
    else:
        return 1 + count_digits(n // 10)

num = int(input("Enter a number: "))
print(f"Number of digits in {num}: {count_digits(num)}")


print("\n" + "=" * 50)
print("BONUS PROBLEM 2: Sum of Digits")
print("=" * 50)

"""
Write a recursive function to find the sum of digits of a number.
"""

def sum_of_digits(n):
    n = abs(n)
    if n < 10:
        return n                        # Base case
    else:
        return (n % 10) + sum_of_digits(n // 10)

num = int(input("Enter a number: "))
print(f"Sum of digits of {num}: {sum_of_digits(num)}")


print("\n" + "=" * 50)
print("BONUS PROBLEM 3: GCD (Greatest Common Divisor)")
print("=" * 50)

"""
Write a recursive function to find GCD of two numbers using Euclidean algorithm.
"""

def gcd(a, b):
    if b == 0:
        return a                        # Base case
    else:
        return gcd(b, a % b)           # Recursive case

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"GCD of {a} and {b}: {gcd(a, b)}")


print("\n" + "=" * 50)
print("BONUS PROBLEM 4: Check Palindrome")
print("=" * 50)

"""
Write a recursive function to check if a string is a palindrome.
"""

def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Normalize
    if len(s) <= 1:
        return True                     # Base case
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])   # Check middle part

text = input("Enter a string: ")
if is_palindrome(text):
    print(f"'{text}' is a Palindrome!")
else:
    print(f"'{text}' is NOT a Palindrome.")


print("\n" + "=" * 50)
print("BONUS PROBLEM 5: Print Array Elements")
print("=" * 50)

"""
Write a recursive function to print all elements of a list.
"""

def print_list(lst, index=0):
    if index >= len(lst):
        return                          # Base case
    print(lst[index], end=" ")
    print_list(lst, index + 1)          # Recursive call

my_list = [10, 20, 30, 40, 50]
print(f"List: {my_list}")
print("Elements:", end=" ")
print_list(my_list)
print()  # New line
