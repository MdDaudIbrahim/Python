"""
=============================================================================
                    PRACTICE PROBLEMS - LISTS
=============================================================================

This file contains practice problems to help you understand 
lists and list operations in Python.

=============================================================================
"""


# =============================================================================
# PROBLEM 1: Store 3 Favorite Movies
# =============================================================================
"""
Write a Python program to ask the user to enter the names of their 3 
favorite movies and store them in a list.
"""

print("=" * 50)
print("PROBLEM 1: Store 3 Favorite Movies")
print("=" * 50)

movies = []

for i in range(3):
    movie = input("Enter the name of movie: ")
    movies.append(movie)

print("Your favorite movies are:\n", movies)

"""
Example Output:
---------------
Enter the name of movie: Inception
Enter the name of movie: Interstellar
Enter the name of movie: The Matrix
Your favorite movies are:
 ['Inception', 'Interstellar', 'The Matrix']
"""


# =============================================================================
# PROBLEM 2: Check if List is Palindrome
# =============================================================================
"""
Write a Python program to check if a list is a palindrome, meaning the 
list reads the same forward and backward. (Hint: Use the copy() method)
"""

print("\n" + "=" * 50)
print("PROBLEM 2: Check if List is Palindrome")
print("=" * 50)

elements = input("Enter elements (space-separated): ").split()

original_list = elements.copy()
original_list.reverse()
reversed_list = original_list

if elements == reversed_list:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")

"""
Example Output 1:
-----------------
Enter elements: 1 2 1
The list is a palindrome.

Example Output 2:
-----------------
Enter elements: 1 2 3
The list is not a palindrome.
"""


# =============================================================================
# PROBLEM 3: Sum of 5 Numbers in a List
# =============================================================================
"""
Write a Python program that takes 5 numbers as input from the user, 
stores them in a list, and then prints the list along with the sum of 
all the numbers.
"""

print("\n" + "=" * 50)
print("PROBLEM 3: Sum of 5 Numbers in a List")
print("=" * 50)

numbers = []
total = 0

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)
    total += num

print("Your list:", numbers)
print("Sum of all numbers:", total)

"""
Example Output:
---------------
Enter a number: 10
Enter a number: 20
Enter a number: 30
Enter a number: 40
Enter a number: 50
Your list: [10, 20, 30, 40, 50]
Sum of all numbers: 150
"""


# =============================================================================
# BONUS PROBLEMS
# =============================================================================

print("\n" + "=" * 50)
print("BONUS PROBLEM 1: Find Maximum and Minimum")
print("=" * 50)

"""
Write a program to take 5 numbers and find the maximum and minimum.
"""

numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("List:", numbers)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))


print("\n" + "=" * 50)
print("BONUS PROBLEM 2: Remove Duplicates")
print("=" * 50)

"""
Write a program to remove duplicates from a list.
"""

items = input("Enter items (space-separated): ").split()
print("Original list:", items)

unique_items = []
for item in items:
    if item not in unique_items:
        unique_items.append(item)

print("After removing duplicates:", unique_items)


print("\n" + "=" * 50)
print("BONUS PROBLEM 3: Sort List in Ascending and Descending")
print("=" * 50)

"""
Write a program to sort a list in both ascending and descending order.
"""

numbers = []
n = int(input("How many numbers? "))

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("Original list:", numbers)

ascending = sorted(numbers)
print("Ascending order:", ascending)

descending = sorted(numbers, reverse=True)
print("Descending order:", descending)
