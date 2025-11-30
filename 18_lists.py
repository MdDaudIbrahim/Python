"""
=============================================================================
                              LISTS
=============================================================================

What is a List?
---------------
A list is an ordered, changeable (mutable) collection that allows duplicate 
values. It works just like an Array in other programming languages.

Syntax:
    listVariableName = ["item1", "item2", "item3"]

Key Features:
- Ordered: Items have a defined order
- Mutable: Can be changed after creation
- Allows duplicates
- Can contain mixed data types (numbers, strings, etc.)

=============================================================================
                        COMMON LIST OPERATIONS
=============================================================================

Operation       Example                     Description
---------       -------                     -----------
Access item     fruits[0]                   'apple'
Change item     fruits[1] = "mango"         Replaces 'banana' with 'mango'
Add item        fruits.append("orange")     Adds to end
Insert item     fruits.insert(1, "kiwi")    Inserts at index 1
Remove item     fruits.remove("apple")      Removes 'apple'
Pop item        fruits.pop()                Removes last item
Length          len(fruits)                 Number of items
Sort            fruits.sort()               Sorts list
Reverse         fruits.reverse()            Reverses list
Slicing         fruits[1:3]                 'banana', 'cherry'

=============================================================================
"""


# =============================================================================
# CREATING A LIST
# =============================================================================

print("=" * 50)
print("CREATING A LIST")
print("=" * 50)

fruits = ["apple", "banana", "cherry"]
print("fruits =", fruits)

# Mixed data types
mixed_list = [1, "hello", 3.14, True]
print("mixed_list =", mixed_list)

# Empty list
empty_list = []
print("empty_list =", empty_list)


# =============================================================================
# ACCESS ITEM
# =============================================================================
"""
We can access elements in a list using indexing.
Syntax: list_name[index]

Note: Indexing starts at 0, negative indexing starts from the end.
"""

print("\n" + "=" * 50)
print("ACCESS ITEM")
print("=" * 50)

fruits = ["apple", "banana", "cherry"]

print(f"fruits = {fruits}")
print(f"fruits[0] = {fruits[0]}")     # Output: apple
print(f"fruits[1] = {fruits[1]}")     # Output: banana
print(f"fruits[-1] = {fruits[-1]}")   # Output: cherry (last item)
print(f"fruits[-2] = {fruits[-2]}")   # Output: banana


# =============================================================================
# CHANGE ITEM
# =============================================================================
"""
Lists are mutable, so you can change the value of an item by its index.
Syntax: list_name[index] = new_value

Notes:
- Index must be valid (within range)
- Only one item is updated at a time
"""

print("\n" + "=" * 50)
print("CHANGE ITEM")
print("=" * 50)

fruits = ["apple", "banana", "cherry"]
print("Before:", fruits)

fruits[1] = "mango"
print("After:", fruits)

# Output: ['apple', 'mango', 'cherry']


# =============================================================================
# ADD ITEM
# =============================================================================
"""
You can add items to a list using:
- append()  : Add at the end
- insert()  : Add at specific position
- extend()  : Add multiple items
"""

print("\n" + "=" * 50)
print("ADD ITEM")
print("=" * 50)

# append() - Add at the end
print("--- append() ---")
fruits = ["apple", "banana"]
print("Before:", fruits)
fruits.append("cherry")
print("After append:", fruits)
# Output: ['apple', 'banana', 'cherry']

# insert(index, item) - Add at specific position
print("\n--- insert() ---")
fruits = ["apple", "banana"]
print("Before:", fruits)
fruits.insert(1, "orange")
print("After insert(1, 'orange'):", fruits)
# Output: ['apple', 'orange', 'banana']

# extend() - Add multiple items
print("\n--- extend() ---")
fruits = ["apple", "banana"]
print("Before:", fruits)
fruits.extend(["grape", "melon"])
print("After extend:", fruits)
# Output: ['apple', 'banana', 'grape', 'melon']


# =============================================================================
# INSERT ITEM
# =============================================================================
"""
To add an item at a specific position, use the insert() method.
Syntax: list_name.insert(index, item)

Notes:
- Index starts at 0
- Shifts elements to the right
- If index > length, item is added at the end
"""

print("\n" + "=" * 50)
print("INSERT ITEM")
print("=" * 50)

fruits = ["apple", "banana", "cherry"]
print("Before:", fruits)

fruits.insert(1, "orange")
print("After insert(1, 'orange'):", fruits)
# Output: ['apple', 'orange', 'banana', 'cherry']


# =============================================================================
# REMOVE ITEM
# =============================================================================
"""
We can remove items using the remove() method.
Syntax: list_name.remove(item)

Notes:
- Removes FIRST occurrence of the specified item
- If item not found, raises ValueError
"""

print("\n" + "=" * 50)
print("REMOVE ITEM")
print("=" * 50)

fruits = ["apple", "banana", "cherry"]
print("Before:", fruits)

fruits.remove("banana")
print("After remove('banana'):", fruits)
# Output: ['apple', 'cherry']


# =============================================================================
# POP ITEM
# =============================================================================
"""
The pop() method removes an item by index and returns it.
Syntax: list_name.pop(index)  # index is optional

Notes:
- If no index given, removes LAST item
- Returns the removed item
- If index out of range, raises IndexError
"""

print("\n" + "=" * 50)
print("POP ITEM")
print("=" * 50)

fruits = ["apple", "banana", "cherry"]
print("Before:", fruits)

removed = fruits.pop()
print("Removed item:", removed)
print("After pop():", fruits)
# Output: ['apple', 'banana']

# Pop with index
fruits = ["apple", "banana", "cherry"]
removed = fruits.pop(1)
print("\nRemoved fruits.pop(1):", removed)
print("After:", fruits)
# Output: ['apple', 'cherry']


# =============================================================================
# LIST LENGTH
# =============================================================================

print("\n" + "=" * 50)
print("LIST LENGTH")
print("=" * 50)

fruits = ["apple", "banana", "cherry", "date"]
print(f"fruits = {fruits}")
print(f"len(fruits) = {len(fruits)}")   # Output: 4


# =============================================================================
# LIST METHODS
# =============================================================================
"""
Common List Methods:
- append(item)      : Add item at end
- insert(i, item)   : Insert item at index i
- remove(item)      : Remove first occurrence
- pop(i)            : Remove and return item at index i
- sort()            : Sort in ascending order
- sort(reverse=True): Sort in descending order
- reverse()         : Reverse the list
- copy()            : Return a copy of the list
- clear()           : Remove all items
- index(item)       : Return index of item
- count(item)       : Count occurrences
"""

print("\n" + "=" * 50)
print("LIST METHODS")
print("=" * 50)

# sort()
print("--- sort() ---")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print("Before:", numbers)
numbers.sort()
print("After sort():", numbers)
# Output: [1, 1, 2, 3, 4, 5, 6, 9]

# sort(reverse=True)
print("\n--- sort(reverse=True) ---")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort(reverse=True)
print("After sort(reverse=True):", numbers)
# Output: [9, 6, 5, 4, 3, 2, 1, 1]

# reverse()
print("\n--- reverse() ---")
numbers = [1, 2, 3, 4, 5]
print("Before:", numbers)
numbers.reverse()
print("After reverse():", numbers)
# Output: [5, 4, 3, 2, 1]

# copy()
print("\n--- copy() ---")
original = [1, 2, 3]
copied = original.copy()
print("Original:", original)
print("Copied:", copied)

# index() and count()
print("\n--- index() and count() ---")
fruits = ["apple", "banana", "apple", "cherry"]
print(f"fruits = {fruits}")
print(f"fruits.index('banana') = {fruits.index('banana')}")  # 1
print(f"fruits.count('apple') = {fruits.count('apple')}")    # 2


# =============================================================================
# LIST SLICING
# =============================================================================

print("\n" + "=" * 50)
print("LIST SLICING")
print("=" * 50)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"fruits = {fruits}")
print(f"fruits[1:3] = {fruits[1:3]}")     # ['banana', 'cherry']
print(f"fruits[:3] = {fruits[:3]}")       # ['apple', 'banana', 'cherry']
print(f"fruits[2:] = {fruits[2:]}")       # ['cherry', 'date', 'elderberry']
print(f"fruits[-3:-1] = {fruits[-3:-1]}") # ['cherry', 'date']
