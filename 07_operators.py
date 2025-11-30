"""
=============================================================================
                         TYPES OF OPERATORS
=============================================================================

What are Operators?
-------------------
Python supports several types of operators to perform operations on 
variables and values.

Types of Operators:
-------------------
1. Arithmetic Operators    - Used for math operations
2. Assignment Operators    - Assign or update values
3. Comparison Operators    - Compare values (returns True/False)
4. Logical Operators       - Combine conditions
5. Bitwise Operators       - Work on bits

=============================================================================
"""


# =============================================================================
# 1. ARITHMETIC OPERATORS
# =============================================================================
"""
Used for mathematical operations.

Operator    Name                Example
--------    ----                -------
+           Addition            x + y
-           Subtraction         x - y
*           Multiplication      x * y
/           Division            x / y
%           Modulus (Remainder) x % y
//          Floor Division      x // y
**          Exponentiation      x ** y
"""

print("=" * 50)
print("1. ARITHMETIC OPERATORS")
print("=" * 50)

x = 10
y = 3

print(f"x = {x}, y = {y}")
print(f"x + y = {x + y}")       # Addition: 13
print(f"x - y = {x - y}")       # Subtraction: 7
print(f"x * y = {x * y}")       # Multiplication: 30
print(f"x / y = {x / y}")       # Division: 3.333...
print(f"x % y = {x % y}")       # Modulus: 1
print(f"x // y = {x // y}")     # Floor Division: 3
print(f"x ** y = {x ** y}")     # Exponentiation: 1000


# =============================================================================
# 2. ASSIGNMENT OPERATORS
# =============================================================================
"""
Used to assign values to variables.

Operator    Example     Same As
--------    -------     -------
=           x = 5       x = 5
+=          x += 3      x = x + 3
-=          x -= 3      x = x - 3
*=          x *= 3      x = x * 3
/=          x /= 3      x = x / 3
"""

print("\n" + "=" * 50)
print("2. ASSIGNMENT OPERATORS")
print("=" * 50)

x = 10          # Assignment
print(f"x = {x}")

x += 5          # x = x + 5
print(f"x += 5 → x = {x}")

x -= 3          # x = x - 3
print(f"x -= 3 → x = {x}")

x *= 2          # x = x * 2
print(f"x *= 2 → x = {x}")

x /= 4          # x = x / 4
print(f"x /= 4 → x = {x}")


# =============================================================================
# 3. COMPARISON OPERATORS
# =============================================================================
"""
Used to compare two values. Returns True or False.

Operator    Name                    Example
--------    ----                    -------
==          Equal                   x == y
!=          Not equal               x != y
>           Greater than            x > y
<           Less than               x < y
>=          Greater than or equal   x >= y
<=          Less than or equal      x <= y
"""

print("\n" + "=" * 50)
print("3. COMPARISON OPERATORS")
print("=" * 50)

x = 10
y = 5

print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")      # Equal: False
print(f"x != y: {x != y}")      # Not equal: True
print(f"x > y: {x > y}")        # Greater than: True
print(f"x < y: {x < y}")        # Less than: False
print(f"x >= y: {x >= y}")      # Greater or equal: True
print(f"x <= y: {x <= y}")      # Less or equal: False


# =============================================================================
# 4. LOGICAL OPERATORS
# =============================================================================
"""
Used to combine conditional statements.

Operator    Description                             Example
--------    -----------                             -------
and         Returns True if both statements true    x > 5 and x < 15
or          Returns True if one statement true      x < 5 or x > 15
not         Reverses the result                     not(x > 5)
"""

print("\n" + "=" * 50)
print("4. LOGICAL OPERATORS")
print("=" * 50)

x = 10
y = 5

print(f"x = {x}, y = {y}")

# AND - both conditions must be True
print(f"x > 5 and y > 3: {x > 5 and y > 3}")     # True and True = True
print(f"x > 5 and y > 10: {x > 5 and y > 10}")   # True and False = False

# OR - at least one condition must be True
print(f"x > 15 or y > 3: {x > 15 or y > 3}")     # False or True = True
print(f"x > 15 or y > 10: {x > 15 or y > 10}")   # False or False = False

# NOT - reverses the result
print(f"not(x > 5): {not(x > 5)}")               # not True = False
print(f"not(x > 15): {not(x > 15)}")             # not False = True


# =============================================================================
# 5. BITWISE OPERATORS
# =============================================================================
"""
Work on bits and perform bit-by-bit operations.

Operator    Name        Description
--------    ----        -----------
&           AND         Sets bit to 1 if both bits are 1
|           OR          Sets bit to 1 if one bit is 1
^           XOR         Sets bit to 1 if only one bit is 1
~           NOT         Inverts all the bits
<<          Left shift  Shift left by pushing zeros from right
>>          Right shift Shift right by pushing copies from left
"""

print("\n" + "=" * 50)
print("5. BITWISE OPERATORS")
print("=" * 50)

a = 5   # Binary: 0101
b = 3   # Binary: 0011

print(f"a = {a} (binary: {bin(a)})")
print(f"b = {b} (binary: {bin(b)})")

print(f"a & b = {a & b}")       # AND: 0101 & 0011 = 0001 = 1
print(f"a | b = {a | b}")       # OR:  0101 | 0011 = 0111 = 7
print(f"a ^ b = {a ^ b}")       # XOR: 0101 ^ 0011 = 0110 = 6
print(f"~a = {~a}")             # NOT: ~0101 = -6
print(f"a << 1 = {a << 1}")     # Left shift: 0101 << 1 = 1010 = 10
print(f"a >> 1 = {a >> 1}")     # Right shift: 0101 >> 1 = 0010 = 2


# =============================================================================
# COMBINED EXAMPLE
# =============================================================================

print("\n" + "=" * 50)
print("COMBINED EXAMPLE")
print("=" * 50)

x = 10            # Assignment
y = 5             # Assignment

print(x + y)      # Arithmetic: 15
print(x > y)      # Comparison: True
print(x != y)     # Comparison: True
print(x and y)    # Logical: 5 (returns y if both truthy)
