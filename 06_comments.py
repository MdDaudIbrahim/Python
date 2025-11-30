"""
=============================================================================
                         COMMENTS IN PYTHON
=============================================================================

What are Comments?
------------------
Comments are notes in the code that are IGNORED by Python during execution.
They help explain the code for humans (developers).

Why use Comments?
-----------------
1. Explain what the code does
2. Make code easier to understand
3. Leave notes for yourself or other developers
4. Temporarily disable code during testing

=============================================================================
"""


# =============================================================================
# TYPE 1: SINGLE-LINE COMMENTS
# =============================================================================
"""
Single-line comments start with the # symbol.
Everything after # on that line is ignored by Python.
"""

# This is a single-line comment
print("Hello")  # This prints Hello

# The line below prints a greeting message
print("Welcome to Python!")

# You can comment out code to disable it:
# print("This line will NOT execute")

print("This line WILL execute")


# =============================================================================
# TYPE 2: MULTI-LINE COMMENTS
# =============================================================================
"""
Multi-line comments use triple quotes: ''' ''' or  \"\"\" \"\"\"
They can span multiple lines.

Note: Triple quotes are technically multi-line strings, 
but are often used as multi-line comments.
"""

# Example using triple single quotes:
'''
This is a
multi-line comment
using single quotes
'''
print("Hi")

# Example using triple double quotes:
"""
This is another
multi-line comment
using double quotes
"""
print("Hello Again!")


# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

# Calculate the area of a rectangle
# Formula: Area = length × width

length = 10  # length in meters
width = 5    # width in meters

area = length * width  # calculating area

print(f"Area of rectangle: {area} square meters")  # display result


"""
This section calculates the area of a circle.
Formula: Area = π × r²
where:
    π (pi) = 3.14159
    r = radius of the circle
"""

pi = 3.14159     # value of pi
radius = 7       # radius in centimeters

circle_area = pi * (radius ** 2)  # area calculation

print(f"Area of circle: {circle_area} square centimeters")


# =============================================================================
# GOOD COMMENTING PRACTICES
# =============================================================================

# ✅ GOOD: Clear and helpful comments
# Calculate discount price
original_price = 100
discount_percent = 20
discount_amount = original_price * (discount_percent / 100)
final_price = original_price - discount_amount
print(f"Final price after {discount_percent}% discount: ${final_price}")

# ❌ BAD: Obvious comments that don't add value
# x = 5          # assign 5 to x (this comment is unnecessary!)
# print(x)       # print x (this is obvious!)

# ✅ BETTER: Explain WHY, not WHAT
x = 5  # Initial retry count for API calls
print(f"Starting with {x} retries")
