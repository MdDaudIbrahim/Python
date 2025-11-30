"""
=============================================================================
                              DATA TYPES
=============================================================================

What are Data Types?
--------------------
In Python, data types define the kind of value a variable holds.

Basic Data Types:
-----------------
Type        Example             Description
----        -------             -----------
int         x = 10              Whole numbers
float       pi = 3.14           Decimal numbers
str         name = "Mohsin"     Text (string of characters)
bool        is_valid = True     Boolean (True or False)

=============================================================================
"""

# How to See the Data Type in Python
# -----------------------------------
# Use the type() function
# Syntax: type(variable)


# Integer Example
x = 10
print(type(x))         # Output: <class 'int'>

# String Example
name = "Mohsin"
print(type(name))      # Output: <class 'str'>

# Float Example
price = 3.99
print(type(price))     # Output: <class 'float'>

# Boolean Example
is_valid = True
print(type(is_valid))  # Output: <class 'bool'>


"""
Output:
-------
<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
"""


# More Examples with Detailed Explanation
# ----------------------------------------

print("\n--- INTEGER (int) ---")
age = 25
count = -10
big_number = 1000000
print(f"age = {age}, type: {type(age)}")
print(f"count = {count}, type: {type(count)}")
print(f"big_number = {big_number}, type: {type(big_number)}")


print("\n--- FLOAT (float) ---")
temperature = 98.6
pi = 3.14159
negative_float = -45.67
print(f"temperature = {temperature}, type: {type(temperature)}")
print(f"pi = {pi}, type: {type(pi)}")
print(f"negative_float = {negative_float}, type: {type(negative_float)}")


print("\n--- STRING (str) ---")
first_name = "Mohsin"
message = 'Hello World'
empty_string = ""
print(f"first_name = {first_name}, type: {type(first_name)}")
print(f"message = {message}, type: {type(message)}")
print(f"empty_string = '{empty_string}', type: {type(empty_string)}")


print("\n--- BOOLEAN (bool) ---")
is_active = True
is_deleted = False
print(f"is_active = {is_active}, type: {type(is_active)}")
print(f"is_deleted = {is_deleted}, type: {type(is_deleted)}")


# Type Conversion (Bonus)
# -----------------------
print("\n--- TYPE CONVERSION ---")

# Convert int to float
num_int = 10
num_float = float(num_int)
print(f"int to float: {num_int} -> {num_float}")

# Convert float to int (removes decimal)
decimal_num = 3.99
whole_num = int(decimal_num)
print(f"float to int: {decimal_num} -> {whole_num}")

# Convert int to string
number = 100
text = str(number)
print(f"int to string: {number} -> '{text}'")
