"""
=============================================================================
                PRACTICE PROBLEMS - DICTIONARY
=============================================================================

This file contains practice problems to help you understand 
dictionaries and their operations in Python.

=============================================================================
"""


# =============================================================================
# PROBLEM 1: Dictionary with Multiple Meanings
# =============================================================================
"""
Store the following word meanings in a Python dictionary, where each word 
can have multiple meanings.

table → "a piece of furniture", "list of facts & figures"
cat → "a small animal"
"""

print("=" * 50)
print("PROBLEM 1: Dictionary with Multiple Meanings")
print("=" * 50)

dictionary = {
    "table": ["a piece of furniture", "list of facts & figures"],
    "cat": ["a small animal"]
}

# Printing the dictionary
print("Dictionary:", dictionary)
print()

print("Table meanings:", dictionary["table"])
print("Cat meanings:", dictionary["cat"])

# Access individual meanings
print("\nFirst meaning of 'table':", dictionary["table"][0])
print("Second meaning of 'table':", dictionary["table"][1])

"""
Output:
-------
Dictionary: {'table': ['a piece of furniture', 'list of facts & figures'], 
             'cat': ['a small animal']}

Table meanings: ['a piece of furniture', 'list of facts & figures']
Cat meanings: ['a small animal']
"""


# =============================================================================
# PROBLEM 2: Store Subject Marks
# =============================================================================
"""
Write a Python program to enter marks of 3 subjects from the user and store 
them in a dictionary. Start with an empty dictionary and add subject–marks 
one by one using the subject name as the key and the marks as the value.
"""

print("\n" + "=" * 50)
print("PROBLEM 2: Store Subject Marks")
print("=" * 50)

marks_dict = {}

for i in range(3):
    subject = input("Enter subject name: ")
    marks = int(input(f"Enter marks for {subject}: "))
    marks_dict[subject] = marks

print("\nMarks Dictionary:", marks_dict)

# Calculate total and average
total = sum(marks_dict.values())
average = total / len(marks_dict)
print(f"Total Marks: {total}")
print(f"Average: {average:.2f}")

"""
Example Output:
---------------
Enter subject name: Physics
Enter marks for Physics: 99
Enter subject name: English
Enter marks for English: 78
Enter subject name: Math
Enter marks for Math: 100
Marks Dictionary: {'Physics': 99, 'English': 78, 'Math': 100}
Total Marks: 277
Average: 92.33
"""


# =============================================================================
# BONUS PROBLEMS
# =============================================================================

print("\n" + "=" * 50)
print("BONUS PROBLEM 1: Student Information System")
print("=" * 50)

"""
Create a student information system that stores name, age, and grade.
Allow the user to add, view, and search for students.
"""

students = {}

# Add some sample students
students["S001"] = {"name": "Alice", "age": 20, "grade": "A"}
students["S002"] = {"name": "Bob", "age": 21, "grade": "B"}
students["S003"] = {"name": "Charlie", "age": 19, "grade": "A"}

print("Current Students:")
for sid, info in students.items():
    print(f"  {sid}: {info['name']}, Age: {info['age']}, Grade: {info['grade']}")

# Search for a student
search_id = input("\nEnter student ID to search: ")
if search_id in students:
    student = students[search_id]
    print(f"Found: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
else:
    print("Student not found!")


print("\n" + "=" * 50)
print("BONUS PROBLEM 2: Word Frequency Counter")
print("=" * 50)

"""
Count the frequency of each word in a sentence.
"""

sentence = input("Enter a sentence: ")
words = sentence.lower().split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("\nWord Frequency:")
for word, count in word_count.items():
    print(f"  '{word}': {count}")


print("\n" + "=" * 50)
print("BONUS PROBLEM 3: Phone Book")
print("=" * 50)

"""
Create a simple phone book application.
"""

phone_book = {}

print("Phone Book Application")
print("Enter contacts (type 'done' to finish):")

while True:
    name = input("Enter name (or 'done'): ")
    if name.lower() == 'done':
        break
    phone = input(f"Enter phone number for {name}: ")
    phone_book[name] = phone

print("\nYour Phone Book:")
if phone_book:
    for name, phone in phone_book.items():
        print(f"  {name}: {phone}")
else:
    print("  Phone book is empty!")

# Search for contact
if phone_book:
    search = input("\nEnter name to search: ")
    if search in phone_book:
        print(f"{search}'s number: {phone_book[search]}")
    else:
        print(f"{search} not found in phone book.")


print("\n" + "=" * 50)
print("BONUS PROBLEM 4: Inventory Management")
print("=" * 50)

"""
Create a simple inventory system with product name, quantity, and price.
"""

inventory = {
    "apple": {"quantity": 50, "price": 1.50},
    "banana": {"quantity": 30, "price": 0.75},
    "orange": {"quantity": 40, "price": 2.00}
}

print("Current Inventory:")
print("-" * 40)
print(f"{'Product':<15}{'Quantity':<12}{'Price':<10}{'Value':<10}")
print("-" * 40)

total_value = 0
for product, details in inventory.items():
    value = details["quantity"] * details["price"]
    total_value += value
    print(f"{product:<15}{details['quantity']:<12}${details['price']:<9.2f}${value:<9.2f}")

print("-" * 40)
print(f"{'Total Inventory Value:':<27}${total_value:.2f}")
