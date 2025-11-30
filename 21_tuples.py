"""
=============================================================================
                              TUPLES
=============================================================================

What is a Tuple?
----------------
A tuple is an ordered, immutable (unchangeable) collection of items. 
It is similar to a list but CANNOT be modified after creation.

Syntax:
    my_tuple = (item1, item2, item3)

Key Features:
- Defined using parentheses ()
- IMMUTABLE: Cannot change, add, or remove items after creation
- Ordered: Items have a defined order
- Allows duplicate values
- Can contain mixed data types

=============================================================================
"""


# =============================================================================
# CREATING A TUPLE
# =============================================================================

print("=" * 50)
print("CREATING A TUPLE")
print("=" * 50)

fruits = ("apple", "banana", "cherry")
print("fruits =", fruits)

# Mixed data types
mixed_tuple = (1, "hello", 3.14, True)
print("mixed_tuple =", mixed_tuple)

# Empty tuple
empty_tuple = ()
print("empty_tuple =", empty_tuple)


# =============================================================================
# TUPLE WITH ONE ITEM
# =============================================================================
"""
IMPORTANT: To create a tuple with one item, you MUST include a comma!
Without the comma, Python treats it as a regular value.
"""

print("\n" + "=" * 50)
print("TUPLE WITH ONE ITEM")
print("=" * 50)

# Correct way - with comma
one_item = ("apple",)
print(f"one_item = {one_item}")
print(f"type(one_item) = {type(one_item)}")   # <class 'tuple'>

print()

# Wrong way - without comma (NOT a tuple!)
not_tuple = ("apple")
print(f"not_tuple = {not_tuple}")
print(f"type(not_tuple) = {type(not_tuple)}")  # <class 'str'>


# =============================================================================
# ACCESSING TUPLE ITEMS
# =============================================================================
"""
Access tuple items using indexing, just like lists.
Indexing starts at 0.
"""

print("\n" + "=" * 50)
print("ACCESSING TUPLE ITEMS")
print("=" * 50)

fruits = ("apple", "banana", "cherry", "date")
print(f"fruits = {fruits}")

print(f"fruits[0] = {fruits[0]}")     # apple
print(f"fruits[2] = {fruits[2]}")     # cherry
print(f"fruits[-1] = {fruits[-1]}")   # date (last item)


# =============================================================================
# TUPLE SLICING
# =============================================================================

print("\n" + "=" * 50)
print("TUPLE SLICING")
print("=" * 50)

fruits = ("apple", "banana", "cherry", "date", "elderberry")
print(f"fruits = {fruits}")

print(f"fruits[1:3] = {fruits[1:3]}")     # ('banana', 'cherry')
print(f"fruits[:3] = {fruits[:3]}")       # ('apple', 'banana', 'cherry')
print(f"fruits[2:] = {fruits[2:]}")       # ('cherry', 'date', 'elderberry')


# =============================================================================
# TUPLES ARE IMMUTABLE
# =============================================================================
"""
Tuples CANNOT be changed after creation.
The following operations will raise errors:

fruits[0] = "mango"     # ❌ TypeError
fruits.append("grape")  # ❌ AttributeError
fruits.remove("apple")  # ❌ AttributeError
"""

print("\n" + "=" * 50)
print("TUPLES ARE IMMUTABLE")
print("=" * 50)

fruits = ("apple", "banana", "cherry")
print(f"fruits = {fruits}")
print("Trying to change fruits[0] would raise: TypeError")
print("Tuples cannot be modified after creation!")

# Workaround: Convert to list, modify, convert back
print("\n--- Workaround: Convert to List ---")
fruits = ("apple", "banana", "cherry")
print("Original tuple:", fruits)

fruits_list = list(fruits)      # Convert to list
fruits_list[0] = "mango"        # Modify
fruits = tuple(fruits_list)     # Convert back to tuple

print("Modified tuple:", fruits)


# =============================================================================
# TUPLE METHODS
# =============================================================================
"""
Tuples have only 2 built-in methods:
- count(item)   : Count how many times an item appears
- index(item)   : Find the index of an item

Other useful functions:
- len(tuple)    : Length of the tuple
- max(tuple)    : Maximum value
- min(tuple)    : Minimum value
"""

print("\n" + "=" * 50)
print("TUPLE METHODS")
print("=" * 50)

fruits = ("apple", "banana", "cherry", "apple", "apple")
print(f"fruits = {fruits}")

# len()
print(f"\nlen(fruits) = {len(fruits)}")           # 5

# count()
print(f"fruits.count('apple') = {fruits.count('apple')}")  # 3

# index()
print(f"fruits.index('banana') = {fruits.index('banana')}") # 1

# max() and min() with numbers
numbers = (10, 5, 20, 15, 8)
print(f"\nnumbers = {numbers}")
print(f"max(numbers) = {max(numbers)}")    # 20
print(f"min(numbers) = {min(numbers)}")    # 5


# =============================================================================
# LOOPING THROUGH A TUPLE
# =============================================================================

print("\n" + "=" * 50)
print("LOOPING THROUGH A TUPLE")
print("=" * 50)

fruits = ("apple", "banana", "cherry")

print("Using for loop:")
for fruit in fruits:
    print(f"  - {fruit}")

print("\nUsing for loop with index:")
for i in range(len(fruits)):
    print(f"  Index {i}: {fruits[i]}")


# =============================================================================
# TUPLE UNPACKING
# =============================================================================
"""
Tuple unpacking allows you to assign tuple items to individual variables.
"""

print("\n" + "=" * 50)
print("TUPLE UNPACKING")
print("=" * 50)

# Basic unpacking
coordinates = (10, 20, 30)
x, y, z = coordinates

print(f"coordinates = {coordinates}")
print(f"x = {x}, y = {y}, z = {z}")

# Unpacking with *
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers

print(f"\nnumbers = {numbers}")
print(f"first = {first}")
print(f"middle = {middle}")
print(f"last = {last}")
