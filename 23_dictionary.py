"""
=============================================================================
                              DICTIONARY
=============================================================================

What is a Dictionary?
---------------------
A dictionary is an unordered, mutable collection that stores key:value pairs.
It allows you to store and retrieve data using unique keys.

Syntax:
    my_dict = {
        "key1": "value1",
        "key2": "value2"
    }

Key Features:
- Keys must be UNIQUE
- Values can be any data type
- Defined using curly braces {}
- Mutable (can be changed after creation)
- Unordered (before Python 3.7) / Ordered (Python 3.7+)

=============================================================================
                        COMMON DICTIONARY METHODS
=============================================================================

Method                      Description
------                      -----------
dict.keys()                 Returns all keys
dict.values()               Returns all values
dict.items()                Returns all key-value pairs
dict.get("key")             Gets value for key, returns None if absent
dict["key"] = value         Adds or updates a key-value pair
dict.pop("key")             Removes a key-value pair

=============================================================================
"""


# =============================================================================
# CREATING A DICTIONARY
# =============================================================================

print("=" * 50)
print("CREATING A DICTIONARY")
print("=" * 50)

student = {
    "name": "Mohsin",
    "age": 21,
    "department": "CSE"
}

print("student =", student)
print("student['name'] =", student["name"])   # Output: Mohsin

# Empty dictionary
empty_dict = {}
print("\nempty_dict =", empty_dict)

# Dictionary with mixed value types
mixed_dict = {
    "name": "Alice",
    "age": 25,
    "grades": [90, 85, 88],
    "is_active": True
}
print("mixed_dict =", mixed_dict)


# =============================================================================
# dict.keys() METHOD
# =============================================================================
"""
The .keys() method returns a view object containing all the keys 
from a dictionary.

Syntax: dictionary.keys()
"""

print("\n" + "=" * 50)
print("dict.keys() METHOD")
print("=" * 50)

student = {
    "name": "Alif",
    "age": 21,
    "dept": "CSE"
}

print(f"student = {student}")
print(f"student.keys() = {student.keys()}")

# Convert to list
keys_list = list(student.keys())
print(f"list(student.keys()) = {keys_list}")


# =============================================================================
# dict.values() METHOD
# =============================================================================
"""
The .values() method returns a view object containing all the values 
in the dictionary.

Syntax: dictionary.values()
"""

print("\n" + "=" * 50)
print("dict.values() METHOD")
print("=" * 50)

student = {
    "name": "Alif",
    "age": 21,
    "dept": "CSE"
}

print(f"student = {student}")
print(f"student.values() = {student.values()}")

# Convert to list
values_list = list(student.values())
print(f"list(student.values()) = {values_list}")


# =============================================================================
# dict.get("key") METHOD
# =============================================================================
"""
The .get() method returns the value for the specified key.
If the key is not found, it returns None (or a default value if provided),
without causing an error.

Syntax: dictionary.get("key", default_value?)

Difference from dict["key"]:
- student["dept"] → ❌ Raises KeyError if key doesn't exist
- student.get("dept") → ✅ Returns None (or default)
"""

print("\n" + "=" * 50)
print("dict.get() METHOD")
print("=" * 50)

student = {
    "name": "Nihan",
    "age": 21
}

print(f"student = {student}")
print(f"student.get('name') = {student.get('name')}")        # Nihan
print(f"student.get('dept') = {student.get('dept')}")        # None
print(f"student.get('dept', 'N/A') = {student.get('dept', 'N/A')}")  # N/A

# Compare with dict["key"]
print("\n--- Comparison ---")
print("student.get('dept') returns: None (safe)")
print("student['dept'] would raise: KeyError (unsafe)")


# =============================================================================
# dict.items() METHOD
# =============================================================================
"""
The .items() method returns a view object containing all key-value pairs 
as tuples.

Syntax: dictionary.items()
"""

print("\n" + "=" * 50)
print("dict.items() METHOD")
print("=" * 50)

student = {
    "name": "Jam",
    "age": 21,
    "dept": "CSE"
}

print(f"student = {student}")
print(f"student.items() = {student.items()}")

# Looping through items
print("\nLooping through items:")
for key, value in student.items():
    print(f"  {key}: {value}")


# =============================================================================
# ADDING/UPDATING: dict["key"] = value
# =============================================================================
"""
The dict["key"] = value syntax is used to:
- Add a new key-value pair (if key doesn't exist)
- Update the value of an existing key (if key exists)

Syntax: dictionary["key"] = value
"""

print("\n" + "=" * 50)
print("ADDING/UPDATING VALUES")
print("=" * 50)

student = {
    "name": "Mohsin",
    "age": 21
}
print("Original:", student)

# Add new key-value
student["dept"] = "CSE"
print("After adding 'dept':", student)

# Update existing value
student["age"] = 22
print("After updating 'age':", student)


# =============================================================================
# dict.pop("key") METHOD
# =============================================================================
"""
The .pop("key") method removes the specified key from the dictionary 
and returns its value.

Syntax: dictionary.pop("key", default_value?)

Note: If key doesn't exist and no default is provided, raises KeyError.
"""

print("\n" + "=" * 50)
print("dict.pop() METHOD")
print("=" * 50)

student = {
    "name": "Alice",
    "age": 21,
    "dept": "CSE"
}
print("Original:", student)

removed_value = student.pop("age")
print(f"Removed value: {removed_value}")
print("After pop('age'):", student)

# Pop with default value (key doesn't exist)
result = student.pop("grade", "Not found")
print(f"\npop('grade', 'Not found'): {result}")


# =============================================================================
# OTHER USEFUL METHODS
# =============================================================================

print("\n" + "=" * 50)
print("OTHER USEFUL METHODS")
print("=" * 50)

student = {
    "name": "Bob",
    "age": 20,
    "dept": "EEE"
}

# clear() - removes all items
demo = {"a": 1, "b": 2}
print(f"demo = {demo}")
demo.clear()
print(f"After clear(): {demo}")

# copy() - returns a copy
student_copy = student.copy()
print(f"\nstudent.copy() = {student_copy}")

# update() - updates dictionary with another dictionary
student.update({"grade": "A", "age": 21})
print(f"After update(): {student}")

# Check if key exists
print(f"\n'name' in student: {'name' in student}")
print(f"'email' in student: {'email' in student}")


# =============================================================================
# LOOPING THROUGH DICTIONARY
# =============================================================================

print("\n" + "=" * 50)
print("LOOPING THROUGH DICTIONARY")
print("=" * 50)

student = {
    "name": "Charlie",
    "age": 22,
    "dept": "CSE"
}

print("--- Loop through keys ---")
for key in student:
    print(f"  {key}")

print("\n--- Loop through values ---")
for value in student.values():
    print(f"  {value}")

print("\n--- Loop through key-value pairs ---")
for key, value in student.items():
    print(f"  {key}: {value}")
