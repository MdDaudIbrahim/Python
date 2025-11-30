"""
=============================================================================
                        NESTED DICTIONARY
=============================================================================

What is a Nested Dictionary?
----------------------------
A nested dictionary is a dictionary inside another dictionary.
It allows you to represent complex structured data.

Syntax:
    nested_dict = {
        "key1": {
            "subkey1": value1,
            "subkey2": value2
        },
        "key2": {
            "subkey1": value1,
            "subkey2": value2
        }
    }

=============================================================================
"""


# =============================================================================
# CREATING A NESTED DICTIONARY
# =============================================================================

print("=" * 50)
print("CREATING A NESTED DICTIONARY")
print("=" * 50)

students = {
    "23-50194-1": {
        "name": "Mohsin",
        "age": 21
    },
    "23-50187-1": {
        "name": "Jam",
        "age": 22
    }
}

print("students =")
for student_id, info in students.items():
    print(f"  {student_id}: {info}")


# =============================================================================
# ACCESSING NESTED VALUES
# =============================================================================
"""
To access nested values, chain the keys together.
Syntax: dictionary["outer_key"]["inner_key"]
"""

print("\n" + "=" * 50)
print("ACCESSING NESTED VALUES")
print("=" * 50)

students = {
    "23-50194-1": {
        "name": "Mohsin",
        "age": 21
    },
    "23-50187-1": {
        "name": "Jam",
        "age": 22
    }
}

# Access nested value
print(f"students['23-50194-1']['name'] = {students['23-50194-1']['name']}")
print(f"students['23-50187-1']['age'] = {students['23-50187-1']['age']}")


# =============================================================================
# MODIFYING NESTED VALUES
# =============================================================================
"""
Syntax: dictionary["outer_key"]["inner_key"] = new_value
"""

print("\n" + "=" * 50)
print("MODIFYING NESTED VALUES")
print("=" * 50)

students = {
    "23-50194-1": {
        "name": "Mohsin",
        "age": 21
    },
    "23-50187-1": {
        "name": "Jam",
        "age": 22
    }
}

print("Before modification:")
print(f"  23-50194-1 age: {students['23-50194-1']['age']}")

# Modify nested value
students["23-50194-1"]["age"] = 23

print("\nAfter modification:")
print(f"  23-50194-1 age: {students['23-50194-1']['age']}")


# =============================================================================
# ADDING NEW INNER DICTIONARY
# =============================================================================
"""
You can add a completely new inner dictionary to a nested dictionary.
Syntax: dictionary["new_key"] = {"subkey": value, ...}
"""

print("\n" + "=" * 50)
print("ADDING NEW INNER DICTIONARY")
print("=" * 50)

students = {
    "23-50194-1": {
        "name": "Mohsin",
        "age": 24
    },
    "23-50187-1": {
        "name": "Jam",
        "age": 22
    }
}

print("Before adding new students:")
print(f"  Total students: {len(students)}")

# Add new inner dictionaries
students["23-50200-1"] = {
    "name": "Nihan",
    "age": 23
}

students["23-50186-1"] = {
    "name": "Alif",
    "age": 21
}

print("\nAfter adding new students:")
print(f"  Total students: {len(students)}")

print("\nAll students:")
print(f"  23-50186-1: {students['23-50186-1']}")
print(f"  23-50187-1: {students['23-50187-1']}")
print(f"  23-50194-1: {students['23-50194-1']}")
print(f"  23-50200-1: {students['23-50200-1']}")


# =============================================================================
# LOOPING THROUGH NESTED DICTIONARY
# =============================================================================

print("\n" + "=" * 50)
print("LOOPING THROUGH NESTED DICTIONARY")
print("=" * 50)

students = {
    "23-50194-1": {"name": "Mohsin", "age": 21, "dept": "CSE"},
    "23-50187-1": {"name": "Jam", "age": 22, "dept": "CSE"},
    "23-50200-1": {"name": "Nihan", "age": 23, "dept": "EEE"}
}

print("Student Details:")
print("-" * 40)

for student_id, info in students.items():
    print(f"ID: {student_id}")
    for key, value in info.items():
        print(f"  {key}: {value}")
    print()


# =============================================================================
# NESTED DICTIONARY WITH LISTS
# =============================================================================

print("=" * 50)
print("NESTED DICTIONARY WITH LISTS")
print("=" * 50)

students = {
    "23-50194-1": {
        "name": "Mohsin",
        "subjects": ["Math", "Physics", "Programming"],
        "grades": [90, 85, 95]
    },
    "23-50187-1": {
        "name": "Jam",
        "subjects": ["Math", "Chemistry", "Biology"],
        "grades": [88, 92, 78]
    }
}

print("Student Mohsin's subjects:", students["23-50194-1"]["subjects"])
print("Student Jam's first grade:", students["23-50187-1"]["grades"][0])

# Calculate average grade
mohsin_grades = students["23-50194-1"]["grades"]
average = sum(mohsin_grades) / len(mohsin_grades)
print(f"\nMohsin's average grade: {average:.2f}")
