"""
=============================================================================
                              SETS
=============================================================================

What is a Set?
--------------
A Set is an unordered, unindexed collection of UNIQUE elements.
It is useful when we want to store items without duplicates.

Syntax:
    my_set = {1, 2, 3}

Key Features:
- Unordered: Items have no defined order
- Unindexed: Cannot access items by index
- Unique: No duplicate values allowed
- Mutable: Can add/remove items (but items must be immutable)

=============================================================================
                        COMMON SET METHODS
=============================================================================

Operation           Code Example                Result
---------           ------------                ------
Add item            my_set.add(4)               Adds 4 to the set
Remove item         my_set.remove(2)            Removes 2, raises error if not found
Discard item        my_set.discard(2)           Removes 2, no error if not found
Pop random item     my_set.pop()                Removes a random element
Clear set           my_set.clear()              Removes all items
Union               a.union(b) or a | b         All unique items from both sets
Intersection        a.intersection(b) or a & b  Common items only
Difference          a.difference(b) or a - b    Items in a but not in b

=============================================================================
"""


# =============================================================================
# CREATING A SET
# =============================================================================

print("=" * 50)
print("CREATING A SET")
print("=" * 50)

# Basic set
my_set = {1, 2, 3}
print("my_set =", my_set)

# Duplicates are automatically removed!
numbers = {1, 2, 3, 2, 1}
print("numbers = {1, 2, 3, 2, 1} →", numbers)
# Output: {1, 2, 3}

# Empty set (use set(), not {})
empty_set = set()
print("empty_set =", empty_set)

# Set from a list
list_to_set = set([1, 2, 2, 3, 3, 3])
print("set([1, 2, 2, 3, 3, 3]) =", list_to_set)


# =============================================================================
# ADD ITEM
# =============================================================================
"""
To add a new element to a set, use the .add() method.
Syntax: set_name.add(item)

Notes:
- If the item already exists, it won't be added again
- Order is not guaranteed when printing a set
"""

print("\n" + "=" * 50)
print("ADD ITEM - .add()")
print("=" * 50)

fruits = {"apple", "banana"}
print("Before:", fruits)

fruits.add("cherry")
print("After add('cherry'):", fruits)

# Adding duplicate (won't be added)
fruits.add("apple")
print("After add('apple') again:", fruits)  # No change


# =============================================================================
# REMOVE ITEM
# =============================================================================
"""
Use .remove() to remove an item.
Syntax: set_name.remove(item)

Note: Raises KeyError if the element is not found!
"""

print("\n" + "=" * 50)
print("REMOVE ITEM - .remove()")
print("=" * 50)

fruits = {"apple", "banana", "cherry"}
print("Before:", fruits)

fruits.remove("banana")
print("After remove('banana'):", fruits)

# fruits.remove("orange")  # ❌ Would raise KeyError!


# =============================================================================
# DISCARD ITEM
# =============================================================================
"""
Use .discard() to remove an item safely.
Syntax: set_name.discard(item)

Note: Does NOT raise an error if the item is missing!
"""

print("\n" + "=" * 50)
print("DISCARD ITEM - .discard()")
print("=" * 50)

fruits = {"apple", "banana", "cherry"}
print("Before:", fruits)

fruits.discard("banana")
print("After discard('banana'):", fruits)

fruits.discard("orange")  # No error!
print("After discard('orange'):", fruits)  # No change, no error


# =============================================================================
# POP RANDOM ITEM
# =============================================================================
"""
The .pop() method removes and returns a random element from a set 
because sets are unordered.

Syntax: set_name.pop()

Note: Raises KeyError if the set is empty.
"""

print("\n" + "=" * 50)
print("POP RANDOM ITEM - .pop()")
print("=" * 50)

colors = {"red", "green", "blue"}
print("Before:", colors)

removed_item = colors.pop()
print("Removed:", removed_item)
print("Remaining:", colors)


# =============================================================================
# CLEAR SET
# =============================================================================
"""
To remove all elements from a set, use the .clear() method.
Syntax: set_name.clear()
"""

print("\n" + "=" * 50)
print("CLEAR SET - .clear()")
print("=" * 50)

fruits = {"apple", "banana", "cherry"}
print("Before:", fruits)

fruits.clear()
print("After clear():", fruits)  # set()


# =============================================================================
# UNION SETS
# =============================================================================
"""
The union of sets returns a new set containing ALL unique elements 
from the sets involved.

Syntax:
    set1.union(set2, set3, ...)
    # or
    set1 | set2 | set3

Notes:
- Duplicates are automatically removed
- Original sets remain unchanged
"""

print("\n" + "=" * 50)
print("UNION SETS - .union() or |")
print("=" * 50)

a = {"apple", "banana"}
b = {"banana", "cherry"}
c = {"mango"}

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

d = a.union(b)
print(f"\na.union(b) = {d}")

e = a | b | c
print(f"a | b | c = {e}")


# =============================================================================
# INTERSECTION SETS
# =============================================================================
"""
The intersection of sets returns a new set containing only elements 
COMMON to all sets.

Syntax:
    set1.intersection(set2, set3, ...)
    # or
    set1 & set2 & set3

Notes:
- Does not modify the original sets
- Result contains only shared elements
"""

print("\n" + "=" * 50)
print("INTERSECTION SETS - .intersection() or &")
print("=" * 50)

a = {"apple", "banana", "cherry"}
b = {"banana", "cherry", "grape"}
c = {"mango", "cherry", "grape"}

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

d = a.intersection(b)
print(f"\na.intersection(b) = {d}")

e = a & b & c
print(f"a & b & c = {e}")


# =============================================================================
# DIFFERENCE SETS
# =============================================================================
"""
The difference returns a new set containing elements that are 
ONLY in the first set and NOT in the others.

Syntax:
    set1.difference(set2, set3, ...)
    # or
    set1 - set2 - set3

Notes:
- The original sets are not changed
- The set from which we subtract comes first
"""

print("\n" + "=" * 50)
print("DIFFERENCE SETS - .difference() or -")
print("=" * 50)

a = {"apple", "banana", "cherry"}
b = {"banana", "grape"}
c = {"mango", "cherry", "grape"}

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

d = a.difference(b)
print(f"\na.difference(b) = {d}")  # Items in a but not in b

e = a - b - c
print(f"a - b - c = {e}")  # Items in a but not in b or c


# =============================================================================
# OTHER SET OPERATIONS
# =============================================================================

print("\n" + "=" * 50)
print("OTHER SET OPERATIONS")
print("=" * 50)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"a = {a}")
print(f"b = {b}")

# Symmetric difference (items in either set, but not both)
sym_diff = a.symmetric_difference(b)
print(f"\na.symmetric_difference(b) = {sym_diff}")
print(f"a ^ b = {a ^ b}")

# Check if subset
c = {1, 2}
print(f"\nc = {c}")
print(f"c.issubset(a) = {c.issubset(a)}")

# Check if superset
print(f"a.issuperset(c) = {a.issuperset(c)}")

# Check if disjoint (no common elements)
d = {7, 8, 9}
print(f"\nd = {d}")
print(f"a.isdisjoint(d) = {a.isdisjoint(d)}")
