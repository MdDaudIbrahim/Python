"""
=============================================================================
                              KEYWORDS
=============================================================================

What are Keywords?
------------------
Keywords are reserved words in Python. We cannot use them as variable names 
or identifiers. They have special meaning in the language.

List of Python Keywords:
------------------------
False       class       finally     is          return
None        continue    for         lambda      try
True        def         from        nonlocal    while
and         del         global      not         with
as          elif        if          or          yield
assert      else        import      pass        
break       except      in          raise
async       await

=============================================================================
"""

# How to see all keywords in Python
# ----------------------------------

import keyword

print("Total number of keywords:", len(keyword.kwlist))
print("\nList of all Python keywords:")
print(keyword.kwlist)


# Example: Correct use of keywords
# ---------------------------------

print("\n--- CORRECT USE OF KEYWORDS ---")

# Using 'if' keyword
if True:
    print("This is a keyword example using 'if'")

# Using 'for' keyword
for i in range(3):
    print(f"Loop iteration: {i}")

# Using 'def' keyword to define a function
def greet():
    return "Hello!"

print(greet())


# Example: WRONG use of keywords (DO NOT DO THIS!)
# -------------------------------------------------
"""
The following code would cause an ERROR:

class = "Math"      # ❌ Error! 'class' is a keyword
for = 10            # ❌ Error! 'for' is a keyword
if = "hello"        # ❌ Error! 'if' is a keyword
True = 5            # ❌ Error! 'True' is a keyword

These will raise: SyntaxError: invalid syntax
"""


# Correct alternatives:
# ---------------------
print("\n--- CORRECT ALTERNATIVES ---")

class_name = "Math"     # ✅ Use descriptive names
for_count = 10          # ✅ Add prefix or suffix
if_condition = "hello"  # ✅ Make it meaningful
is_true = True          # ✅ Use proper variable names

print(f"class_name = {class_name}")
print(f"for_count = {for_count}")
print(f"if_condition = {if_condition}")
print(f"is_true = {is_true}")


# Check if a word is a keyword
# -----------------------------
print("\n--- CHECK IF A WORD IS A KEYWORD ---")

words = ["class", "name", "for", "hello", "True", "print"]

for word in words:
    if keyword.iskeyword(word):
        print(f"'{word}' is a keyword - Cannot use as variable name")
    else:
        print(f"'{word}' is NOT a keyword - Can use as variable name")
