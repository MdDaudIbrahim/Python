"""
=============================================================================
                    TAKING USER INPUT IN A LIST
=============================================================================

We can take list input from a user using:
1. split() method - for space-separated input
2. Loop - for multiple separate inputs

=============================================================================
"""


# =============================================================================
# METHOD 1: Using split()
# =============================================================================
"""
The split() method splits a string into a list based on a delimiter.
By default, it splits by whitespace (spaces).

Syntax: string.split(delimiter)
"""

print("=" * 50)
print("METHOD 1: Using split()")
print("=" * 50)

names = input("Enter names (space-separated): ").split()
print("Names list:", names)

"""
Example:
--------
Enter names (space-separated): Alice Bob Charlie
Names list: ['Alice', 'Bob', 'Charlie']
"""

# Split by comma
print("\n--- Split by comma ---")
items = input("Enter items (comma-separated): ").split(",")
print("Items list:", items)


# =============================================================================
# METHOD 2: Using a Loop
# =============================================================================
"""
Use a loop to get multiple inputs one by one.
"""

print("\n" + "=" * 50)
print("METHOD 2: Using a Loop")
print("=" * 50)

n = int(input("How many items? "))
items = []

for i in range(n):
    item = input(f"Enter item {i+1}: ")
    items.append(item)

print("Items list:", items)

"""
Example:
--------
How many items? 3
Enter item 1: apple
Enter item 2: banana
Enter item 3: cherry
Items list: ['apple', 'banana', 'cherry']
"""


# =============================================================================
# Taking Numeric Input
# =============================================================================

print("\n" + "=" * 50)
print("TAKING NUMERIC INPUT")
print("=" * 50)

n = int(input("How many numbers? "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("Numbers list:", numbers)
print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))
