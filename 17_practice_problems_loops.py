"""
=============================================================================
                    PRACTICE PROBLEMS - LOOPS
=============================================================================

This file contains practice problems to help you understand 
for loops, while loops, break, continue, and pass in Python.

=============================================================================
"""


# =============================================================================
# PROBLEM 1: Print 1 to 5 using while loop
# =============================================================================
"""
Write a Python program to print numbers from 1 to 5 using a while loop.
"""

print("=" * 50)
print("PROBLEM 1: Print 1 to 5 (while loop)")
print("=" * 50)

i = 1
while i <= 5:
    print(i)
    i += 1

"""
Output:
-------
1
2
3
4
5
"""


# =============================================================================
# PROBLEM 2: Print 5 to 1 using while loop
# =============================================================================
"""
Write a Python program to print numbers from 5 to 1 using a while loop.
"""

print("\n" + "=" * 50)
print("PROBLEM 2: Print 5 to 1 (while loop)")
print("=" * 50)

i = 5
while i >= 1:
    print(i)
    i -= 1

"""
Output:
-------
5
4
3
2
1
"""


# =============================================================================
# PROBLEM 3: Sum of 1 to n using while loop
# =============================================================================
"""
Write a Python program to input a number n and print the sum of all 
numbers from 1 to n using a while loop.
"""

print("\n" + "=" * 50)
print("PROBLEM 3: Sum of 1 to n (while loop)")
print("=" * 50)

n = int(input("Enter a number: "))

total = 0
i = 1
while i <= n:
    total += i
    i += 1

print(f"Sum of 1 to {n} is: {total}")

"""
Example Output:
---------------
Enter a number: 5
Sum of 1 to 5 is: 15
(1 + 2 + 3 + 4 + 5 = 15)
"""


# =============================================================================
# PROBLEM 4: Multiplication Table using while loop
# =============================================================================
"""
Write a Python program to input a number n and print its multiplication 
table using a while loop.
"""

print("\n" + "=" * 50)
print("PROBLEM 4: Multiplication Table (while loop)")
print("=" * 50)

n = int(input("Enter a number: "))

i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1

"""
Example Output:
---------------
Enter a number: 11
11 x 1 = 11
11 x 2 = 22
11 x 3 = 33
11 x 4 = 44
11 x 5 = 55
11 x 6 = 66
11 x 7 = 77
11 x 8 = 88
11 x 9 = 99
11 x 10 = 110
"""


# =============================================================================
# PROBLEM 5: Print 1 to 5 using for loop
# =============================================================================
"""
Write a Python program to print numbers from 1 to 5 using a for loop & range().
"""

print("\n" + "=" * 50)
print("PROBLEM 5: Print 1 to 5 (for loop)")
print("=" * 50)

for i in range(1, 6):
    print(i)

"""
Output:
-------
1
2
3
4
5
"""


# =============================================================================
# PROBLEM 6: Print 5 to 1 using for loop
# =============================================================================
"""
Write a Python program to print numbers from 5 to 1 using a for loop & range().
"""

print("\n" + "=" * 50)
print("PROBLEM 6: Print 5 to 1 (for loop)")
print("=" * 50)

for i in range(5, 0, -1):
    print(i)

"""
Output:
-------
5
4
3
2
1
"""


# =============================================================================
# PROBLEM 7: Sum of 1 to n using for loop
# =============================================================================
"""
Write a Python program to input a number n and print the sum of all 
numbers from 1 to n using a for loop & range().
"""

print("\n" + "=" * 50)
print("PROBLEM 7: Sum of 1 to n (for loop)")
print("=" * 50)

n = int(input("Enter a number: "))

total = 0
for i in range(1, n + 1):
    total += i

print(f"Sum of 1 to {n} is: {total}")

"""
Example Output:
---------------
Enter a number: 10
Sum of 1 to 10 is: 55
"""


# =============================================================================
# PROBLEM 8: Sum with break (stop at -1)
# =============================================================================
"""
Write a Python program that takes numbers as input from the user using a 
while loop. The loop should stop if the user enters -1. Print the sum of 
all entered numbers (excluding -1).
"""

print("\n" + "=" * 50)
print("PROBLEM 8: Sum with break (stop at -1)")
print("=" * 50)

total = 0

while True:
    num = int(input("Enter a number (-1 to stop): "))
    if num == -1:
        break
    total += num

print("Total sum is:", total)

"""
Example Output:
---------------
Enter a number (-1 to stop): 10
Enter a number (-1 to stop): 5
Enter a number (-1 to stop): 3
Enter a number (-1 to stop): 2
Enter a number (-1 to stop): 1
Enter a number (-1 to stop): -1
Total sum is: 21
"""


# =============================================================================
# PROBLEM 9: Print 1 to 10 except 5 (using continue)
# =============================================================================
"""
Write a Python program to print all numbers from 1 to 10 in a line, 
except for number 5, using a for loop and the continue statement.
"""

print("\n" + "=" * 50)
print("PROBLEM 9: Print 1-10 except 5 (continue)")
print("=" * 50)

for i in range(1, 11):
    if i == 5:
        continue
    print(i, end=" ")

print()  # New line at end

"""
Output:
-------
1 2 3 4 6 7 8 9 10
"""


# =============================================================================
# BONUS PROBLEMS
# =============================================================================

print("\n" + "=" * 50)
print("BONUS PROBLEM 1: Print Even Numbers 1-20")
print("=" * 50)

"""
Print all even numbers from 1 to 20 using a for loop.
"""

for i in range(2, 21, 2):
    print(i, end=" ")
print()

# Output: 2 4 6 8 10 12 14 16 18 20


print("\n" + "=" * 50)
print("BONUS PROBLEM 2: Factorial of n")
print("=" * 50)

"""
Calculate the factorial of a number n.
Factorial of 5 = 5 × 4 × 3 × 2 × 1 = 120
"""

n = int(input("Enter a number: "))

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print(f"Factorial of {n} is: {factorial}")


print("\n" + "=" * 50)
print("BONUS PROBLEM 3: Print Pattern")
print("=" * 50)

"""
Print a simple star pattern:
*
**
***
****
*****
"""

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print("*" * i)
