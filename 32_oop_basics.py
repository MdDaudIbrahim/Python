"""
=============================================================================
                OBJECT-ORIENTED PROGRAMMING (OOP)
=============================================================================

What is OOP?
------------
OOP (Object-Oriented Programming) is a programming paradigm that organizes 
code into classes and objects.

Key Concepts of OOP:
--------------------
Concept         Description
-------         -----------
Class           Blueprint for creating objects
Object          Instance of a class
Attribute       Variables inside a class
Method          Functions inside a class
Constructor     __init__() method called when object is created
Self            Refers to the current object

OOP Features:
-------------
Feature         Description
-------         -----------
Encapsulation   Hiding data (using private variables)
Inheritance     One class inherits from another
Polymorphism    Same method behaves differently in different classes
Abstraction     Hiding complex details using abstract classes

=============================================================================
"""


# =============================================================================
# BASIC OOP EXAMPLE
# =============================================================================

print("=" * 50)
print("BASIC OOP EXAMPLE")
print("=" * 50)

class Student:
    def __init__(self, name, age):
        self.name = name        # attribute
        self.age = age

    def greet(self):            # method
        print("Hello, my name is", self.name)
        print("And my age is", self.age)

# Create object
s1 = Student("Mohsin", 22)

# Access method
s1.greet()

# Access attributes directly
print(f"\nDirect access: Name = {s1.name}, Age = {s1.age}")


# =============================================================================
# CLASS AND OBJECTS
# =============================================================================

print("\n" + "=" * 50)
print("CLASS AND OBJECTS")
print("=" * 50)

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")
    
    def start(self):
        print(f"The {self.brand} {self.model} is starting...")

# Create multiple objects
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Honda", "Accord", 2023)
car3 = Car("Tesla", "Model 3", 2024)

print("Car 1:", end=" ")
car1.display_info()

print("Car 2:", end=" ")
car2.display_info()

print("Car 3:", end=" ")
car3.display_info()

print()
car1.start()


# =============================================================================
# CONSTRUCTOR (__init__)
# =============================================================================
"""
The __init__() method is a special method called automatically when 
an object is created. It's used to initialize the object's attributes.

self: Refers to the current instance of the class.
"""

print("\n" + "=" * 50)
print("CONSTRUCTOR (__init__)")
print("=" * 50)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        print(f"Rectangle created: {width} x {height}")
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# Constructor is called automatically
rect = Rectangle(10, 5)

print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")


# =============================================================================
# CLASS VARIABLES VS INSTANCE VARIABLES
# =============================================================================

print("\n" + "=" * 50)
print("CLASS VARIABLES VS INSTANCE VARIABLES")
print("=" * 50)

class Dog:
    # Class variable (shared by all instances)
    species = "Canis familiaris"
    count = 0
    
    def __init__(self, name, age):
        # Instance variables (unique to each instance)
        self.name = name
        self.age = age
        Dog.count += 1  # Increment class variable
    
    def bark(self):
        print(f"{self.name} says: Woof!")

dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)
dog3 = Dog("Charlie", 2)

print(f"Dog species: {Dog.species}")  # Class variable
print(f"Total dogs created: {Dog.count}")  # Class variable

print(f"\ndog1.name = {dog1.name}")  # Instance variable
print(f"dog2.name = {dog2.name}")  # Instance variable

dog1.bark()
dog2.bark()


# =============================================================================
# METHODS
# =============================================================================

print("\n" + "=" * 50)
print("DIFFERENT TYPES OF METHODS")
print("=" * 50)

class MathOperations:
    pi = 3.14159  # Class variable
    
    def __init__(self, value):
        self.value = value
    
    # Instance method
    def square(self):
        return self.value ** 2
    
    # Class method
    @classmethod
    def get_pi(cls):
        return cls.pi
    
    # Static method
    @staticmethod
    def add(a, b):
        return a + b

math_obj = MathOperations(5)

print(f"Instance method - square(5): {math_obj.square()}")
print(f"Class method - get_pi(): {MathOperations.get_pi()}")
print(f"Static method - add(3, 7): {MathOperations.add(3, 7)}")
