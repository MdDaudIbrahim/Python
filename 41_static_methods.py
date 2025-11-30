"""
=============================================================================
                        STATIC METHODS
=============================================================================

What is a Static Method?
------------------------
A static method is a method that does not take self or cls as the 
first argument. It does not depend on class or instance state.

Why Use Static Methods?
- Used when some functionality is logically related to the class, 
  but doesn't need access to class or instance variables.

Defined using:
    @staticmethod

Key Points:
- Decorated with @staticmethod
- No self or cls parameter
- Can be called using class name or object
- Ideal for utility/helper functions related to a class

=============================================================================
"""


# =============================================================================
# BASIC STATIC METHOD EXAMPLE
# =============================================================================

print("=" * 50)
print("BASIC STATIC METHOD EXAMPLE")
print("=" * 50)

class MathTools:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

# Accessing without creating object
print(MathTools.add(5, 3))       # 8
print(MathTools.multiply(4, 6))  # 24

# Can also access via object
tool = MathTools()
print(tool.add(2, 2))            # 4

"""
Output:
-------
8
24
4
"""


# =============================================================================
# COMPARISON: INSTANCE vs CLASS vs STATIC METHODS
# =============================================================================

print("\n" + "=" * 50)
print("INSTANCE vs CLASS vs STATIC METHODS")
print("=" * 50)

class Demo:
    class_variable = "I am a class variable"
    
    def __init__(self, value):
        self.instance_variable = value
    
    # Instance method - has access to instance (self) and class
    def instance_method(self):
        return f"Instance method: {self.instance_variable}"
    
    # Class method - has access to class (cls), not instance
    @classmethod
    def class_method(cls):
        return f"Class method: {cls.class_variable}"
    
    # Static method - no access to instance or class
    @staticmethod
    def static_method():
        return "Static method: Independent of instance and class"

obj = Demo("I am an instance variable")

print(obj.instance_method())   # Uses self
print(Demo.class_method())     # Uses cls
print(Demo.static_method())    # No self or cls

print("\n--- Also callable via object ---")
print(obj.class_method())      # Class method via object
print(obj.static_method())     # Static method via object


# =============================================================================
# PRACTICAL USE CASE - UTILITY CLASS
# =============================================================================

print("\n" + "=" * 50)
print("UTILITY CLASS EXAMPLE")
print("=" * 50)

class StringUtils:
    @staticmethod
    def is_palindrome(text):
        text = text.lower().replace(" ", "")
        return text == text[::-1]
    
    @staticmethod
    def count_vowels(text):
        vowels = "aeiouAEIOU"
        return sum(1 for char in text if char in vowels)
    
    @staticmethod
    def reverse(text):
        return text[::-1]
    
    @staticmethod
    def capitalize_words(text):
        return ' '.join(word.capitalize() for word in text.split())

# Using static methods without creating object
print(f"Is 'radar' a palindrome? {StringUtils.is_palindrome('radar')}")
print(f"Is 'hello' a palindrome? {StringUtils.is_palindrome('hello')}")
print(f"Vowels in 'Hello World': {StringUtils.count_vowels('Hello World')}")
print(f"Reverse of 'Python': {StringUtils.reverse('Python')}")
print(f"Capitalize: {StringUtils.capitalize_words('hello world python')}")


# =============================================================================
# DATE UTILITY CLASS
# =============================================================================

print("\n" + "=" * 50)
print("DATE UTILITY CLASS")
print("=" * 50)

class DateUtils:
    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    @staticmethod
    def days_in_month(month, year):
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            return 29 if DateUtils.is_leap_year(year) else 28
    
    @staticmethod
    def is_valid_date(day, month, year):
        if month < 1 or month > 12:
            return False
        max_days = DateUtils.days_in_month(month, year)
        return 1 <= day <= max_days

print(f"Is 2024 a leap year? {DateUtils.is_leap_year(2024)}")
print(f"Is 2023 a leap year? {DateUtils.is_leap_year(2023)}")
print(f"Days in February 2024: {DateUtils.days_in_month(2, 2024)}")
print(f"Days in February 2023: {DateUtils.days_in_month(2, 2023)}")
print(f"Is 31/4/2023 valid? {DateUtils.is_valid_date(31, 4, 2023)}")
print(f"Is 30/4/2023 valid? {DateUtils.is_valid_date(30, 4, 2023)}")


# =============================================================================
# STATIC METHOD IN A REGULAR CLASS
# =============================================================================

print("\n" + "=" * 50)
print("STATIC METHOD IN A REGULAR CLASS")
print("=" * 50)

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def get_fahrenheit(self):
        return self.celsius * 9/5 + 32
    
    # Static method - doesn't need instance
    @staticmethod
    def celsius_to_fahrenheit(c):
        return c * 9/5 + 32
    
    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9

# Using instance method
temp = Temperature(25)
print(f"25°C = {temp.get_fahrenheit()}°F (instance method)")

# Using static methods without creating object
print(f"100°C = {Temperature.celsius_to_fahrenheit(100)}°F (static method)")
print(f"98.6°F = {Temperature.fahrenheit_to_celsius(98.6):.1f}°C (static method)")


# =============================================================================
# WHEN TO USE STATIC METHODS
# =============================================================================

print("\n" + "=" * 50)
print("WHEN TO USE STATIC METHODS")
print("=" * 50)

print("""
USE STATIC METHODS WHEN:

1. The method doesn't access instance variables (self)
2. The method doesn't access class variables (cls)
3. The functionality is related to the class conceptually
4. You want to group utility functions within a class
5. The method could be a standalone function but fits better in a class

EXAMPLES:
- Validation functions
- Conversion utilities
- Math calculations
- Factory-like helper functions
- String manipulation helpers

DON'T USE STATIC METHODS WHEN:
- You need to access instance attributes
- You need to modify class state
- The method should be inherited and overridden
""")
