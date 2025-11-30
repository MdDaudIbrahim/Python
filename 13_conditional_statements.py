"""
=============================================================================
                        CONDITIONAL STATEMENTS
=============================================================================

What are Conditional Statements?
--------------------------------
Conditional statements let you execute different blocks of code based on 
conditions. They help your program make decisions.

Types of Conditional Statements:
1. if Statement
2. if...else Statement
3. if...elif...else Statement
4. Nested Conditional Statements

Important Notes:
- Conditions use comparison operators (==, !=, >, <, >=, <=)
- Python uses INDENTATION to define blocks (usually 4 spaces)
- Colon (:) is required after the condition

=============================================================================
"""


# =============================================================================
# 1. if STATEMENT
# =============================================================================
"""
The if statement executes a block of code only if the condition is True.

Syntax:
    if condition:
        # code to execute if condition is True
"""

print("=" * 50)
print("1. if STATEMENT")
print("=" * 50)

x = 10
if x > 0:
    print("Positive number")

# Another example
age = 20
if age >= 18:
    print("You are an adult")

print()  # Empty line for spacing

# Multiple conditions in one if
temperature = 35
if temperature > 30:
    print("It's hot outside!")
    print("Stay hydrated!")


# =============================================================================
# 2. if...else STATEMENT
# =============================================================================
"""
The if...else statement executes one block if condition is True,
and another block if condition is False.

Syntax:
    if condition:
        # code if True
    else:
        # code if False
"""

print("\n" + "=" * 50)
print("2. if...else STATEMENT")
print("=" * 50)

x = -5
if x >= 0:
    print("Positive")
else:
    print("Negative")

# Another example
number = 7
if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")


# =============================================================================
# 3. if...elif...else STATEMENT
# =============================================================================
"""
The if...elif...else statement allows checking multiple conditions.
'elif' is short for 'else if'.

Syntax:
    if condition1:
        # code if condition1 is True
    elif condition2:
        # code if condition2 is True
    elif condition3:
        # code if condition3 is True
    else:
        # code if all conditions are False
"""

print("\n" + "=" * 50)
print("3. if...elif...else STATEMENT")
print("=" * 50)

x = 0
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

# Another example - Grade system
print("\n--- Grade System Example ---")
marks = 85

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Marks: {marks}, Grade: {grade}")


# =============================================================================
# 4. NESTED CONDITIONAL STATEMENTS
# =============================================================================
"""
A nested conditional means using one if or else block inside another.
It allows for more complex decision making.

Syntax:
    if condition1:
        if condition2:
            # code if both conditions are True
        else:
            # code if condition1 is True but condition2 is False
    else:
        # code if condition1 is False
"""

print("\n" + "=" * 50)
print("4. NESTED CONDITIONAL STATEMENTS")
print("=" * 50)

num = 15

if num >= 0:
    if num == 0:
        print("Number is Zero")
    else:
        print("Number is Positive")
else:
    print("Number is Negative")

# More complex example
print("\n--- Nested Example: Age and License ---")
age = 20
has_license = True

if age >= 18:
    print("You are an adult.")
    if has_license:
        print("You can drive a car.")
    else:
        print("You need to get a license first.")
else:
    print("You are a minor.")
    print("You cannot drive yet.")


# =============================================================================
# COMPARISON OPERATORS RECAP
# =============================================================================
"""
Comparison Operators used in conditions:

Operator    Meaning                 Example
--------    -------                 -------
==          Equal to                x == 5
!=          Not equal to            x != 5
>           Greater than            x > 5
<           Less than               x < 5
>=          Greater than or equal   x >= 5
<=          Less than or equal      x <= 5
"""

print("\n" + "=" * 50)
print("COMPARISON OPERATORS IN CONDITIONS")
print("=" * 50)

a = 10
b = 20

print(f"a = {a}, b = {b}")
print(f"a == b: {a == b}")    # False
print(f"a != b: {a != b}")    # True
print(f"a > b: {a > b}")      # False
print(f"a < b: {a < b}")      # True
print(f"a >= b: {a >= b}")    # False
print(f"a <= b: {a <= b}")    # True


# =============================================================================
# LOGICAL OPERATORS IN CONDITIONS
# =============================================================================
"""
Logical Operators to combine conditions:

Operator    Meaning                     Example
--------    -------                     -------
and         Both conditions must be True    x > 0 and x < 10
or          At least one must be True       x < 0 or x > 10
not         Reverses the result             not(x > 0)
"""

print("\n" + "=" * 50)
print("LOGICAL OPERATORS IN CONDITIONS")
print("=" * 50)

x = 5

# Using 'and' - both conditions must be True
if x > 0 and x < 10:
    print(f"{x} is between 0 and 10")

# Using 'or' - at least one condition must be True
y = 15
if y < 0 or y > 10:
    print(f"{y} is outside the range 0-10")

# Using 'not' - reverses the result
is_raining = False
if not is_raining:
    print("It's not raining. Go outside!")
