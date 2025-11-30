"""
=============================================================================
                    PRACTICE PROBLEMS - SETS
=============================================================================

This file contains practice problems to help you understand 
sets and their operations in Python.

=============================================================================
"""


# =============================================================================
# PROBLEM 1: Count Unique Subjects (Classrooms Needed)
# =============================================================================
"""
You are given a list of subjects chosen by students. Each unique subject 
needs one classroom. Write a Python program to calculate how many 
classrooms are needed.

subjects = ["python", "java", "C++", "python", "javascript", 
            "java", "python", "java", "C++", "C"]
"""

print("=" * 50)
print("PROBLEM 1: Count Unique Subjects")
print("=" * 50)

subjects = ["python", "java", "C++", "python", "javascript", 
            "java", "python", "java", "C++", "C"]

print("All subjects:", subjects)
print("Total entries:", len(subjects))

unique_subjects = set(subjects)
classrooms_needed = len(unique_subjects)

print("\nUnique subjects:", unique_subjects)
print("Classrooms needed:", classrooms_needed)

"""
Output:
-------
All subjects: ['python', 'java', 'C++', 'python', 'javascript', 
               'java', 'python', 'java', 'C++', 'C']
Total entries: 10

Unique subjects: {'python', 'java', 'C++', 'javascript', 'C'}
Classrooms needed: 5
"""


# =============================================================================
# PROBLEM 2: Store 9 and 9.0 as Separate Values
# =============================================================================
"""
Figure out a way to store both 9 and 9.0 as separate values in a Python set.
Usually, 9 (int) and 9.0 (float) are considered equal in value, 
so a set will treat them as the same.
"""

print("\n" + "=" * 50)
print("PROBLEM 2: Store 9 and 9.0 as Separate Values")
print("=" * 50)

# The problem: 9 and 9.0 are treated as equal
my_set = {9, 9.0}
print(f"{{9, 9.0}} = {my_set}")  # Only {9}

# Why this happens:
print(f"\n9 == 9.0 is {9 == 9.0}")  # True
print(f"type(9) = {type(9)}")
print(f"type(9.0) = {type(9.0)}")

# Solution 1: Using string and int
print("\n--- Solution 1: Using string ---")
my_set = {9, "9.0"}
print(f"{{9, '9.0'}} = {my_set}")

# Solution 2: Store with type info using tuple (Better!)
print("\n--- Solution 2: Using tuple with type ---")
my_set = {(9, int), (9.0, float)}
print(f"{{(9, int), (9.0, float)}} = {my_set}")


# =============================================================================
# BONUS PROBLEMS
# =============================================================================

print("\n" + "=" * 50)
print("BONUS PROBLEM 1: Find Common Friends")
print("=" * 50)

"""
Find common friends between two people.
"""

alice_friends = {"Bob", "Charlie", "David", "Eve"}
bob_friends = {"Charlie", "David", "Frank", "Grace"}

print(f"Alice's friends: {alice_friends}")
print(f"Bob's friends: {bob_friends}")

common_friends = alice_friends.intersection(bob_friends)
print(f"Common friends: {common_friends}")


print("\n" + "=" * 50)
print("BONUS PROBLEM 2: Remove Duplicates from List")
print("=" * 50)

"""
Remove duplicates from a list while preserving some order.
"""

numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1, 2, 3]
print(f"Original list: {numbers}")

unique_numbers = list(set(numbers))
print(f"After removing duplicates: {unique_numbers}")


print("\n" + "=" * 50)
print("BONUS PROBLEM 3: Students in Different Courses")
print("=" * 50)

"""
Find students enrolled only in Math, only in Science, or in both.
"""

math_students = {"Alice", "Bob", "Charlie", "David"}
science_students = {"Charlie", "David", "Eve", "Frank"}

print(f"Math students: {math_students}")
print(f"Science students: {science_students}")

# Students in both courses
both = math_students & science_students
print(f"\nIn BOTH courses: {both}")

# Students only in Math
only_math = math_students - science_students
print(f"ONLY in Math: {only_math}")

# Students only in Science
only_science = science_students - math_students
print(f"ONLY in Science: {only_science}")

# All students
all_students = math_students | science_students
print(f"ALL students: {all_students}")


print("\n" + "=" * 50)
print("BONUS PROBLEM 4: Check for Duplicate Characters")
print("=" * 50)

"""
Check if a string has duplicate characters.
"""

word = input("Enter a word: ")

if len(word) == len(set(word)):
    print(f"'{word}' has NO duplicate characters")
else:
    print(f"'{word}' has duplicate characters")
    
    # Find the duplicates
    seen = set()
    duplicates = set()
    for char in word:
        if char in seen:
            duplicates.add(char)
        seen.add(char)
    print(f"Duplicate characters: {duplicates}")
