"""
=============================================================================
                              FUNCTIONS
=============================================================================

What is a Function?
-------------------
A function is a block of reusable code that performs a specific task.
Functions help make code modular, organized, and reusable.

Why Use Functions?
- Code reusability (write once, use many times)
- Better organization
- Easier debugging
- Improved readability

=============================================================================
"""


# =============================================================================
# DEFINING AND CALLING A FUNCTION
# =============================================================================
"""
Define a Function:              Call a Function:
    def function_name():            function_name()
        # code block

Note: Use 'def' keyword to define a function.
"""

print("=" * 50)
print("DEFINING AND CALLING A FUNCTION")
print("=" * 50)

# Define a function
def greet():
    print("Hello, welcome to Python!")

# Call the function
greet()

# Another example
def say_hello():
    print("Hello!")
    print("How are you?")

print("\nCalling say_hello():")
say_hello()


# =============================================================================
# FUNCTION WITH PARAMETERS
# =============================================================================
"""
Parameters allow you to pass data into a function.

Define:                         Call:
    def function_name(param):       function_name(argument)
        # use param
"""

print("\n" + "=" * 50)
print("FUNCTION WITH PARAMETERS")
print("=" * 50)

def greet(name):
    print("Hello", name)

greet("Mohsin")
greet("Jam")
greet("Alif")
greet("Nihan")


# Multiple parameters
print("\n--- Multiple Parameters ---")

def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce("Alice", 25)
introduce("Bob", 30)


# =============================================================================
# FUNCTION WITH RETURN VALUE
# =============================================================================
"""
The 'return' statement sends a value back to the caller.

def function_name(params):
    # code
    return value
"""

print("\n" + "=" * 50)
print("FUNCTION WITH RETURN VALUE")
print("=" * 50)

def add(a, b):
    return a + b

result = add(3, 5)
print(f"add(3, 5) = {result}")

# Using return value in expressions
total = add(10, 20) + add(5, 5)
print(f"add(10, 20) + add(5, 5) = {total}")


# More examples with return
print("\n--- More Examples ---")

def multiply(a, b):
    return a * b

def square(n):
    return n * n

def is_even(n):
    return n % 2 == 0

print(f"multiply(4, 5) = {multiply(4, 5)}")
print(f"square(7) = {square(7)}")
print(f"is_even(10) = {is_even(10)}")
print(f"is_even(7) = {is_even(7)}")


# =============================================================================
# DEFAULT PARAMETERS
# =============================================================================
"""
You can set default values for parameters.
"""

print("\n" + "=" * 50)
print("DEFAULT PARAMETERS")
print("=" * 50)

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")                    # Uses default greeting
greet("Bob", "Hi")               # Uses custom greeting
greet("Charlie", "Good morning") # Uses custom greeting


# =============================================================================
# KEYWORD ARGUMENTS
# =============================================================================
"""
You can pass arguments by name (keyword), regardless of order.
"""

print("\n" + "=" * 50)
print("KEYWORD ARGUMENTS")
print("=" * 50)

def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

# Using keyword arguments (order doesn't matter)
describe_person(age=25, city="Dhaka", name="Mohsin")


# =============================================================================
# RETURN MULTIPLE VALUES
# =============================================================================
"""
Functions can return multiple values as a tuple.
"""

print("\n" + "=" * 50)
print("RETURN MULTIPLE VALUES")
print("=" * 50)

def get_min_max(numbers):
    return min(numbers), max(numbers)

nums = [5, 2, 8, 1, 9, 3]
minimum, maximum = get_min_max(nums)

print(f"Numbers: {nums}")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")


# =============================================================================
# VARIABLE SCOPE
# =============================================================================
"""
Variables defined inside a function are LOCAL (only accessible inside).
Variables defined outside are GLOBAL (accessible everywhere).
"""

print("\n" + "=" * 50)
print("VARIABLE SCOPE")
print("=" * 50)

global_var = "I am global"

def demo_scope():
    local_var = "I am local"
    print(f"Inside function: {local_var}")
    print(f"Inside function: {global_var}")

demo_scope()
print(f"Outside function: {global_var}")
# print(local_var)  # ❌ Error! local_var is not accessible here


# =============================================================================
# *args AND **kwargs
# =============================================================================
"""
*args: Accept any number of positional arguments
**kwargs: Accept any number of keyword arguments
"""

print("\n" + "=" * 50)
print("*args AND **kwargs")
print("=" * 50)

# *args example
def sum_all(*args):
    return sum(args)

print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")

# **kwargs example
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("\nprint_info(name='Alice', age=25, city='NYC'):")
print_info(name="Alice", age=25, city="NYC")
