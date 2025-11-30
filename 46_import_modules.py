"""
=============================================================================
                        IMPORT IN PYTHON
=============================================================================

What is Importing?
------------------
Importing allows you to use code from other modules (files) in your 
Python program. Modules contain functions, classes, and variables 
that you can reuse.

Ways to Import:
---------------
1. Import entire module
2. Import with alias
3. Import specific functions/variables
4. Import all (not recommended)

Common Modules:
---------------
Module      Purpose
------      -------
math        Math operations
random      Random number generation
datetime    Date and time handling
os          File system operations
sys         System-specific functions

=============================================================================
"""


# =============================================================================
# IMPORTING AN ENTIRE MODULE
# =============================================================================

print("=" * 50)
print("IMPORTING AN ENTIRE MODULE")
print("=" * 50)

import math

print(f"Square root of 16: {math.sqrt(16)}")      # 4.0
print(f"Pi value: {math.pi}")                      # 3.141592653589793
print(f"Ceiling of 4.2: {math.ceil(4.2)}")        # 5
print(f"Floor of 4.8: {math.floor(4.8)}")         # 4
print(f"Power 2^3: {math.pow(2, 3)}")             # 8.0
print(f"Factorial of 5: {math.factorial(5)}")     # 120


# =============================================================================
# IMPORT WITH ALIAS
# =============================================================================
"""
You can give a module a shorter name (alias) using 'as'.
This is useful for modules with long names.
"""

print("\n" + "=" * 50)
print("IMPORT WITH ALIAS")
print("=" * 50)

import math as m

print(f"Pi using alias: {m.pi}")           # 3.141592653589793
print(f"Sqrt using alias: {m.sqrt(100)}")  # 10.0

# Common aliases
import random as rd
import datetime as dt

print(f"Random number: {rd.randint(1, 100)}")
print(f"Today's date: {dt.date.today()}")


# =============================================================================
# IMPORT SPECIFIC FUNCTION OR VARIABLE
# =============================================================================
"""
You can import only what you need using 'from module import item'.
This way, you don't need to use the module name prefix.
"""

print("\n" + "=" * 50)
print("IMPORT SPECIFIC FUNCTION OR VARIABLE")
print("=" * 50)

from math import sqrt, pi, ceil

print(f"sqrt(25) = {sqrt(25)}")   # 5.0 (no need for math.sqrt)
print(f"pi = {pi}")               # 3.141592653589793
print(f"ceil(3.1) = {ceil(3.1)}") # 4

# Import multiple items
from math import sin, cos, tan, radians

angle = 45
print(f"\nTrigonometry (45 degrees):")
print(f"sin(45) = {sin(radians(angle)):.4f}")
print(f"cos(45) = {cos(radians(angle)):.4f}")
print(f"tan(45) = {tan(radians(angle)):.4f}")


# =============================================================================
# IMPORT ALL FUNCTIONS (NOT RECOMMENDED)
# =============================================================================
"""
Using 'from module import *' imports everything.
This is NOT recommended because:
- It can cause naming conflicts
- Makes code harder to read (unclear where functions come from)
- Imports unnecessary items
"""

print("\n" + "=" * 50)
print("IMPORT ALL (NOT RECOMMENDED)")
print("=" * 50)

# from math import *  # Avoid this!
# print(sin(90))

print("Avoid using 'from module import *'")
print("Reasons:")
print("  - Can cause naming conflicts")
print("  - Makes code harder to understand")
print("  - Imports unnecessary items")


# =============================================================================
# COMMON MODULES OVERVIEW
# =============================================================================

print("\n" + "=" * 50)
print("COMMON MODULES OVERVIEW")
print("=" * 50)

# 1. math - Mathematical functions
import math
print("\n1. MATH MODULE:")
print(f"   sqrt(16) = {math.sqrt(16)}")
print(f"   pi = {math.pi}")
print(f"   e = {math.e}")

# 2. random - Random number generation
import random
print("\n2. RANDOM MODULE:")
print(f"   randint(1, 10) = {random.randint(1, 10)}")
print(f"   random() = {random.random():.4f}")

# 3. datetime - Date and time
import datetime
print("\n3. DATETIME MODULE:")
print(f"   Today: {datetime.date.today()}")
print(f"   Now: {datetime.datetime.now().strftime('%H:%M:%S')}")

# 4. os - Operating system functions
import os
print("\n4. OS MODULE:")
print(f"   Current directory: {os.getcwd()}")
print(f"   OS name: {os.name}")

# 5. sys - System-specific functions
import sys
print("\n5. SYS MODULE:")
print(f"   Python version: {sys.version.split()[0]}")
print(f"   Platform: {sys.platform}")
