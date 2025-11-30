"""
=============================================================================
                         INPUT IN PYTHON
=============================================================================

What is input()?
----------------
The input() function is used to take user input in Python.
It always returns a STRING by default.

Syntax:
-------
variable = input("Enter something: ")

=============================================================================
"""


# =============================================================================
# BASIC INPUT
# =============================================================================

print("=" * 50)
print("BASIC INPUT")
print("=" * 50)

# Taking string input
name = input("Enter your name: ")
print("Hello,", name)

"""
Example Output:
---------------
Enter your name: Mohsin Ibna Hossain
Hello, Mohsin Ibna Hossain
"""


# =============================================================================
# CONVERT INPUT TO OTHER TYPES
# =============================================================================
"""
Since input() always returns a string, we need to convert it 
to other types (int, float) when needed.
"""

print("\n" + "=" * 50)
print("CONVERT INPUT TO OTHER TYPES")
print("=" * 50)

# Converts input to integer
age = int(input("Enter your age: "))

# Converts input to float
price = float(input("Enter price: "))

print("Age:", age)
print("Price:", price)

"""
Example Output:
---------------
Enter your age: 23
Enter price: 99.99
Age: 23
Price: 99.99
"""


# =============================================================================
# MORE INPUT EXAMPLES
# =============================================================================

print("\n" + "=" * 50)
print("MORE INPUT EXAMPLES")
print("=" * 50)

# Taking multiple inputs on separate lines
print("\n--- Taking Multiple Inputs ---")
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
print(f"Full name: {first_name} {last_name}")

# Taking input and performing operations
print("\n--- Input with Operations ---")
num = int(input("Enter a number: "))
print(f"Double of {num} is {num * 2}")
print(f"Square of {num} is {num ** 2}")


# =============================================================================
# IMPORTANT NOTES
# =============================================================================
"""
IMPORTANT NOTES:
----------------
1. input() ALWAYS returns a string
2. To do math operations, convert to int or float first
3. If user enters invalid data (e.g., "abc" when int expected), 
   the program will crash with ValueError

Example of what NOT to do:
--------------------------
num = input("Enter number: ")   # Returns string "5"
result = num + 10               # ERROR! Can't add string + int

Correct way:
------------
num = int(input("Enter number: "))   # Converts to int 5
result = num + 10                    # Works! 5 + 10 = 15
"""
