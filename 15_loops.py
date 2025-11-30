"""
=============================================================================
                              LOOPS
=============================================================================

What are Loops?
---------------
Loops are used to execute a block of code repeatedly.

Types of Loops in Python:
1. for Loop - iterates over a sequence
2. while Loop - runs while a condition is True

=============================================================================
"""


# =============================================================================
# 1. for LOOP
# =============================================================================
"""
The for loop is used to iterate over a sequence (list, string, range, etc.)

Syntax:
    for variable in sequence:
        # code to execute

The range() Function:
    range(start?, end, step?)
    
    - start : starting number (default is 0)
    - end   : ending number (NOT included)
    - step  : increment value (default is 1)
"""

print("=" * 50)
print("1. for LOOP")
print("=" * 50)

# Basic for loop with range
print("--- Basic for loop (0 to 4) ---")
for i in range(5):
    print(i)    # Output: 0 1 2 3 4

print("\n--- for loop with start and end ---")
for i in range(1, 6):
    print(i)    # Output: 1 2 3 4 5

print("\n--- for loop with step ---")
for i in range(0, 10, 2):
    print(i)    # Output: 0 2 4 6 8

print("\n--- for loop counting down ---")
for i in range(5, 0, -1):
    print(i)    # Output: 5 4 3 2 1

# Iterating over a string
print("\n--- Iterating over a string ---")
for char in "Python":
    print(char)

# Iterating over a list
print("\n--- Iterating over a list ---")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# =============================================================================
# 2. while LOOP
# =============================================================================
"""
The while loop runs as long as a condition is True.

Syntax:
    while condition:
        # code to execute
        # update condition variable (important!)

Warning: Make sure to update the condition variable to avoid infinite loops!
"""

print("\n" + "=" * 50)
print("2. while LOOP")
print("=" * 50)

# Basic while loop
print("--- Basic while loop (0 to 2) ---")
count = 0
while count < 3:
    print(count)    # Output: 0 1 2
    count += 1

print("\n--- while loop (1 to 5) ---")
i = 1
while i <= 5:
    print(i)
    i += 1

print("\n--- while loop counting down ---")
i = 5
while i >= 1:
    print(i)
    i -= 1


# =============================================================================
# range() FUNCTION DETAILS
# =============================================================================
"""
The range() function returns a sequence of numbers.

Syntax: range(start?, end, step?)

- start : starting number (0 by default)
- end   : ending number (stops BEFORE this number)
- step  : increment/decrement value (1 by default)
"""

print("\n" + "=" * 50)
print("range() FUNCTION EXAMPLES")
print("=" * 50)

print("range(5):", list(range(5)))              # [0, 1, 2, 3, 4]
print("range(1, 6):", list(range(1, 6)))        # [1, 2, 3, 4, 5]
print("range(0, 10, 2):", list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]
print("range(10, 0, -2):", list(range(10, 0, -2)))  # [10, 8, 6, 4, 2]


# =============================================================================
# PRINTING OUTPUT IN A SINGLE LINE
# =============================================================================
"""
By default, print() adds a newline (\n) after each call.
To print on the same line, use the 'end' parameter.

Syntax: print(value, end=" ")

Notes:
- end=" " adds a space instead of a new line
- You can use any character: end="-", end="", end=", " etc.
"""

print("\n" + "=" * 50)
print("PRINTING IN A SINGLE LINE")
print("=" * 50)

print("--- Default print (new line) ---")
for i in range(3):
    print(i)

print("\n--- Using end=' ' (space) ---")
for i in range(5):
    print(i, end=" ")
print()  # New line after

print("\n--- Using end='-' (hyphen) ---")
for i in range(5):
    print(i, end="-")
print()

print("\n--- Using end=', ' (comma) ---")
for i in range(5):
    print(i, end=", ")
print()
