"""
=============================================================================
                              VARIABLES
=============================================================================

What is a Variable?
-------------------
A variable is a name used to store data in memory. 
It acts as a container for values.

How to Declare a Variable:
--------------------------
Syntax:
    variable_name = value

Note: No need to declare the type—Python figures it out automatically!

=============================================================================
                        RULES FOR NAMING VARIABLES
=============================================================================

1. Must start with a letter or underscore (_)
2. Cannot start with a digit
3. Can contain letters, digits, and underscores
4. Case-sensitive (age and Age are different)

Valid names:     name, _count, my_var, name1
Invalid names:   1name, my-var, my var

=============================================================================
"""

# Variable Declaration Examples
# -----------------------------

a = 5               # Integer
pi = 3.14           # Float
is_valid = True     # Boolean
name = "Mohsin"     # String

# Printing the variables
print("Integer value:", a)
print("Float value:", pi)
print("Boolean value:", is_valid)
print("String value:", name)

"""
Output:
-------
Integer value: 5
Float value: 3.14
Boolean value: True
String value: Mohsin
"""


# More Examples of Variables
# --------------------------

# Variables can be reassigned
x = 10
print("x =", x)     # Output: x = 10

x = 20              # Reassigning
print("x =", x)     # Output: x = 20


# Multiple assignment
a, b, c = 1, 2, 3
print(a, b, c)      # Output: 1 2 3


# Same value to multiple variables
x = y = z = 100
print(x, y, z)      # Output: 100 100 100


# Case sensitivity example
age = 25
Age = 30
AGE = 35
print(age, Age, AGE)    # Output: 25 30 35 (all are different variables)
