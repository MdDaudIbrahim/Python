"""
=============================================================================
                         TYPE CONVERSION
=============================================================================

What is Type Conversion?
------------------------
Type Conversion means changing the data type of a value or variable.

There are TWO types of Type Conversion:
1. Implicit Conversion (Automatic) - Python does it automatically
2. Explicit Conversion (Type Casting) - We do it manually

=============================================================================
"""


# =============================================================================
# 1. IMPLICIT CONVERSION (AUTOMATIC)
# =============================================================================
"""
Python automatically converts one data type to another when needed.
This happens without any user intervention.
"""

print("=" * 50)
print("1. IMPLICIT CONVERSION (Automatic)")
print("=" * 50)

x = 10        # int
y = 2.5       # float

print(f"x = {x}, type: {type(x)}")
print(f"y = {y}, type: {type(y)}")

result = x + y
print(f"\nresult = x + y = {result}")
print(f"type(result): {type(result)}")

# Output:
# result = 12.5 (float)
# type(result): <class 'float'>

# Python automatically converted int to float for the operation!


# Another example of implicit conversion
print("\n--- Another Example ---")

a = 5         # int
b = True      # bool (True = 1, False = 0)

result2 = a + b
print(f"a = {a}, b = {b}")
print(f"a + b = {result2}")       # 6 (bool converted to int)
print(f"type(result2): {type(result2)}")


# =============================================================================
# 2. EXPLICIT CONVERSION (TYPE CASTING)
# =============================================================================
"""
We manually convert types using built-in functions:

Syntax:
-------
int()    # Converts to integer
float()  # Converts to float
str()    # Converts to string
bool()   # Converts to boolean
"""

print("\n" + "=" * 50)
print("2. EXPLICIT CONVERSION (Type Casting)")
print("=" * 50)


# --- Converting to Integer using int() ---
print("\n--- int() - Convert to Integer ---")

x = 5.9
print(f"x = {x}")
print(f"int(x) = {int(x)}")       # 5 (decimal part removed)
print(f"type(x) = {type(x)}")     # <class 'float'>

string_num = "123"
print(f"\nstring_num = '{string_num}'")
print(f"int(string_num) = {int(string_num)}")   # 123


# --- Converting to Float using float() ---
print("\n--- float() - Convert to Float ---")

num = 100
print(f"num = {num}")
print(f"float(num) = {float(num)}")     # 100.0
print(f"type(num) = {type(num)}")       # <class 'int'>


# --- Converting to String using str() ---
print("\n--- str() - Convert to String ---")

y = 100
print(f"y = {y}")
print(f"str(y) = '{str(y)}'")     # "100"
print(f"type(y) = {type(y)}")     # <class 'int'>

pi = 3.14159
print(f"\npi = {pi}")
print(f"str(pi) = '{str(pi)}'")   # "3.14159"


# --- Converting to Boolean using bool() ---
print("\n--- bool() - Convert to Boolean ---")

# Non-zero numbers are True, zero is False
print(f"bool(1) = {bool(1)}")       # True
print(f"bool(0) = {bool(0)}")       # False
print(f"bool(-5) = {bool(-5)}")     # True

# Non-empty strings are True, empty string is False
print(f"bool('Hello') = {bool('Hello')}")   # True
print(f"bool('') = {bool('')}")             # False


# =============================================================================
# COMPLETE EXAMPLE
# =============================================================================

print("\n" + "=" * 50)
print("COMPLETE EXAMPLE")
print("=" * 50)

# Example from the notes
x = 5.9
print(f"x = {x}")
print(f"int(x) = {int(x)}")       # 5
print(f"type(x) = {type(x)}")     # <class 'float'>

print()

y = 100
print(f"y = {y}")
print(f"str(y) = '{str(y)}'")     # "100"
print(f"type(y) = {type(y)}")     # <class 'int'>

print()

z = "45"
print(f"z = '{z}'")
print(f"int(z) = {int(z)}")       # 45
print(f"type(z) = {type(z)}")     # <class 'str'>

"""
Output:
-------
5
<class 'float'>

100
<class 'int'>

45
<class 'str'>
"""
