"""
=============================================================================
                              STRINGS
=============================================================================

What is a String?
-----------------
A string is a sequence of characters enclosed in single, double, or triple quotes.

Examples:
    'Hello'         # Single quotes
    "Hello"         # Double quotes
    '''Hello'''     # Triple quotes (multi-line)

=============================================================================
                        COMMON STRING OPERATIONS
=============================================================================

Operation       Example                     Output
---------       -------                     ------
Concatenation   "Hello" + " World"          'Hello World'
Repetition      "Hi" * 3                    'HiHiHi'
Indexing        "Hello"[1]                  'e'
Slicing         "Hello"[1:4]                'ell'
Length          len("Hello")                5
Uppercase       "hello".upper()             'HELLO'
Lowercase       "HELLO".lower()             'hello'
Replace         "apple".replace("a", "A")   'Apple'
Strip           " hello ".strip()           'hello'

=============================================================================
"""


# =============================================================================
# 1. CONCATENATION
# =============================================================================
"""
Concatenation means joining two or more strings together using the + operator.
"""

print("=" * 50)
print("1. CONCATENATION")
print("=" * 50)

str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)   # Output: Hello World


# =============================================================================
# 2. REPETITION
# =============================================================================
"""
Repetition means repeating a string multiple times using the * operator.
Note: Works only with string and integer
"""

print("\n" + "=" * 50)
print("2. REPETITION")
print("=" * 50)

text = "Hi"
result = text * 3
print(result)   # Output: HiHiHi

# More examples
print("-" * 20)         # Output: --------------------
print("Ha" * 5)         # Output: HaHaHaHaHa


# =============================================================================
# 3. INDEXING
# =============================================================================
"""
Indexing is used to access individual characters in a string using their position (index).
Note: Indexing starts at 0

Index:     0   1   2   3   4   5
String:    P   y   t   h   o   n
Negative: -6  -5  -4  -3  -2  -1
"""

print("\n" + "=" * 50)
print("3. INDEXING")
print("=" * 50)

text = "Python"
print(f"text = '{text}'")
print(f"text[0] = '{text[0]}'")   # Output: P
print(f"text[3] = '{text[3]}'")   # Output: h

# Negative indexing: starts from the end
print("\n--- Negative Indexing ---")
print(f"text[-1] = '{text[-1]}'")  # Output: n (last character)
print(f"text[-3] = '{text[-3]}'")  # Output: h

"""
IndexError: Trying to access an index that doesn't exist will raise an error

text = "Python"
print(text[10])  # ❌ IndexError: string index out of range
"""


# =============================================================================
# 4. SLICING
# =============================================================================
"""
Slicing allows you to extract a portion of a string using a range of indices.

Syntax: string[start : end]

Note: Includes characters from start index up to, but NOT including, end.
"""

print("\n" + "=" * 50)
print("4. SLICING")
print("=" * 50)

text = "Python"
print(f"text = '{text}'")
print(f"text[1:4] = '{text[1:4]}'")     # Output: yth
print(f"text[:3] = '{text[:3]}'")       # Output: Pyt (from beginning)
print(f"text[2:] = '{text[2:]}'")       # Output: thon (to end)
print(f"text[-4:-1] = '{text[-4:-1]}'") # Output: tho

# Slicing with step
print("\n--- Slicing with Step ---")
text2 = "Hello World"
print(f"text2 = '{text2}'")
print(f"text2[::2] = '{text2[::2]}'")   # Every 2nd character: HloWrd
print(f"text2[::-1] = '{text2[::-1]}'") # Reverse string: dlroW olleH


# =============================================================================
# 5. LENGTH
# =============================================================================
"""
To find the length (number of characters) in a string, use the built-in len() function.

Syntax: len(string)

Note: Counts all characters, including spaces, symbols, and numbers.
"""

print("\n" + "=" * 50)
print("5. LENGTH")
print("=" * 50)

msg = "Hi there!"
print(f"msg = '{msg}'")
print(f"len(msg) = {len(msg)}")  # Output: 9

# Spaces are counted!
text_with_spaces = "Hello World"
print(f"\ntext_with_spaces = '{text_with_spaces}'")
print(f"len(text_with_spaces) = {len(text_with_spaces)}")  # Output: 11


# =============================================================================
# 6. UPPERCASE
# =============================================================================
"""
To convert all characters in a string to uppercase, use the .upper() method.

Syntax: string.upper()

Notes:
- Doesn't change the original string (strings are immutable).
- Returns a new string with all letters in uppercase.
"""

print("\n" + "=" * 50)
print("6. UPPERCASE")
print("=" * 50)

text = "python"
print(f"text = '{text}'")
print(f"text.upper() = '{text.upper()}'")  # Output: PYTHON
print(f"Original text = '{text}'")          # Still 'python' (unchanged)


# =============================================================================
# 7. LOWERCASE
# =============================================================================
"""
To convert all characters in a string to lowercase, use the .lower() method.

Syntax: string.lower()

Notes:
- Returns a new string in lowercase.
- Useful for case-insensitive comparisons.
"""

print("\n" + "=" * 50)
print("7. LOWERCASE")
print("=" * 50)

text = "HELLO"
print(f"text = '{text}'")
print(f"text.lower() = '{text.lower()}'")  # Output: hello


# =============================================================================
# 8. REPLACE
# =============================================================================
"""
The .replace() method is used to replace parts of a string with another string.

Syntax: string.replace(old, new)

Notes:
- It does not change the original string.
- We can chain .replace() multiple times if needed.
"""

print("\n" + "=" * 50)
print("8. REPLACE")
print("=" * 50)

text = "I like apples"
print(f"text = '{text}'")
print(f"text.replace('apples', 'oranges') = '{text.replace('apples', 'oranges')}'")
# Output: I like oranges

# Chaining replace
text2 = "apple apple apple"
print(f"\ntext2 = '{text2}'")
print(f"text2.replace('apple', 'orange') = '{text2.replace('apple', 'orange')}'")
# Output: orange orange orange


# =============================================================================
# 9. STRIP
# =============================================================================
"""
The .strip() method is used to remove whitespace or specified characters 
from the start and end of a string.

Syntax:
    string.strip()          # removes spaces
    string.strip(chars)     # removes specified characters

Notes:
- Use .lstrip() to remove from the left only.
- Use .rstrip() to remove from the right only.
"""

print("\n" + "=" * 50)
print("9. STRIP")
print("=" * 50)

text = "  Hello  "
print(f"text = '{text}'")
print(f"text.strip() = '{text.strip()}'")      # Output: Hello

name = "***Mohsin***"
print(f"\nname = '{name}'")
print(f"name.strip('*') = '{name.strip('*')}'")  # Output: Mohsin

# lstrip and rstrip
text2 = "   Hello   "
print(f"\ntext2 = '{text2}'")
print(f"text2.lstrip() = '{text2.lstrip()}'")  # Output: 'Hello   '
print(f"text2.rstrip() = '{text2.rstrip()}'")  # Output: '   Hello'


# =============================================================================
# 10. OTHER STRING FUNCTIONS
# =============================================================================
"""
Additional useful string functions:
- endswith()    : checks if string ends with specified suffix
- capitalize()  : capitalizes first character
- find()        : returns index of first occurrence
- count()       : counts occurrences of substring
"""

print("\n" + "=" * 50)
print("10. OTHER STRING FUNCTIONS")
print("=" * 50)

str1 = "I am a coder."

print(f"str1 = '{str1}'")
print(f"str1.endswith('er.') = {str1.endswith('er.')}")     # True
print(f"str1.capitalize() = '{str1.capitalize()}'")          # I am a coder.
print(f"str1.find('a') = {str1.find('a')}")                  # 2 (first 'a')
print(f"str1.count('a') = {str1.count('a')}")                # 2 (counts all 'a')

# More useful methods
print("\n--- More String Methods ---")
text = "hello world"
print(f"text = '{text}'")
print(f"text.title() = '{text.title()}'")           # Hello World
print(f"text.startswith('hello') = {text.startswith('hello')}")  # True
print(f"text.split() = {text.split()}")             # ['hello', 'world']
print(f"'-'.join(['a','b','c']) = '{'-'.join(['a','b','c'])}'")  # a-b-c
