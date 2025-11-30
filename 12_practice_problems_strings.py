"""
=============================================================================
                    PRACTICE PROBLEMS - STRINGS
=============================================================================

This file contains practice problems to help you understand 
string operations and methods in Python.

=============================================================================
"""


# =============================================================================
# PROBLEM 1: Find Length of First Name
# =============================================================================
"""
Write a Program to input user's first name & print its length.
"""

print("=" * 50)
print("PROBLEM 1: Find Length of First Name")
print("=" * 50)

first_name = input("Enter first name: ")

length = len(first_name)
print("Length of first name is:", length)

"""
Example Output:
---------------
Enter first name: Mohsin
Length of first name is: 6
"""


# =============================================================================
# PROBLEM 2: Count Dollar Sign Occurrences
# =============================================================================
"""
Write a Python program to initialize a string and find how many times 
the character '$' appears in it.
text = "He bought a pen for $5 and a book for $10, total $15."
"""

print("\n" + "=" * 50)
print("PROBLEM 2: Count Dollar Sign Occurrences")
print("=" * 50)

text = "He bought a pen for $5 and a book for $10, total $15."
count = text.count('$')

print(f"Text: {text}")
print("The character '$' appears", count, "time(s).")

"""
Output:
-------
Text: He bought a pen for $5 and a book for $10, total $15.
The character '$' appears 3 time(s).
"""


# =============================================================================
# PROBLEM 3: Convert String to Uppercase
# =============================================================================
"""
Write a Python program to initialize a string containing a sentence, and then
convert and print the entire string in uppercase letters using a string function.
"""

print("\n" + "=" * 50)
print("PROBLEM 3: Convert String to Uppercase")
print("=" * 50)

sentence = "Learning Python is fun."
upper_sentence = sentence.upper()

print(f"Original: {sentence}")
print("Uppercase:", upper_sentence)

"""
Output:
-------
Original: Learning Python is fun.
Uppercase: LEARNING PYTHON IS FUN.
"""


# =============================================================================
# BONUS PROBLEMS
# =============================================================================

print("\n" + "=" * 50)
print("BONUS PROBLEM 1: Reverse a String")
print("=" * 50)

"""
Write a program to input a string and print it in reverse.
"""

text = input("Enter a string: ")
reversed_text = text[::-1]
print("Reversed:", reversed_text)

"""
Example Output:
---------------
Enter a string: Python
Reversed: nohtyP
"""


print("\n" + "=" * 50)
print("BONUS PROBLEM 2: Count Vowels")
print("=" * 50)

"""
Write a program to count the number of vowels in a given string.
"""

text = input("Enter a string: ")
text_lower = text.lower()

vowels = "aeiou"
count = 0

for char in text_lower:
    if char in vowels:
        count += 1

print(f"Number of vowels in '{text}': {count}")

"""
Example Output:
---------------
Enter a string: Hello World
Number of vowels in 'Hello World': 3
"""


print("\n" + "=" * 50)
print("BONUS PROBLEM 3: Replace Spaces with Hyphens")
print("=" * 50)

"""
Write a program to replace all spaces in a string with hyphens.
"""

text = input("Enter a sentence: ")
new_text = text.replace(" ", "-")

print("Original:", text)
print("Modified:", new_text)

"""
Example Output:
---------------
Enter a sentence: Hello World Python
Original: Hello World Python
Modified: Hello-World-Python
"""


print("\n" + "=" * 50)
print("BONUS PROBLEM 4: Check Palindrome")
print("=" * 50)

"""
Write a program to check if a string is a palindrome.
(A palindrome reads the same forwards and backwards)
"""

text = input("Enter a string: ")
text_clean = text.lower().replace(" ", "")  # Remove spaces and convert to lowercase

if text_clean == text_clean[::-1]:
    print(f"'{text}' is a Palindrome!")
else:
    print(f"'{text}' is NOT a Palindrome.")

"""
Example Output 1:
-----------------
Enter a string: madam
'madam' is a Palindrome!

Example Output 2:
-----------------
Enter a string: hello
'hello' is NOT a Palindrome.
"""
