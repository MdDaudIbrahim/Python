"""
=============================================================================
                        INHERITANCE
=============================================================================

What is Inheritance?
--------------------
Inheritance allows a class (child) to acquire properties and methods 
from another class (parent), promoting code reusability.

Syntax:
    class Parent:
        # Parent class content

    class Child(Parent):
        # Child class inherits Parent

Types of Inheritance in Python:
-------------------------------
Type                    Description
----                    -----------
Single Inheritance      One child class inherits one parent
Multiple Inheritance    One class inherits from multiple parents
Multilevel Inheritance  Inheritance across multiple levels
Hierarchical Inheritance Multiple child classes from one parent
Hybrid Inheritance      Combination of multiple types

=============================================================================
"""


# =============================================================================
# SINGLE INHERITANCE
# =============================================================================

print("=" * 50)
print("SINGLE INHERITANCE")
print("=" * 50)

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print(f"{self.name} says: Woof!")

# Create Dog object
dog = Dog("Buddy")
dog.speak()  # Inherited method
dog.bark()   # Own method


# =============================================================================
# MULTIPLE INHERITANCE
# =============================================================================
"""
One class inherits from multiple parent classes.
"""

print("\n" + "=" * 50)
print("MULTIPLE INHERITANCE")
print("=" * 50)

class A:
    def methodA(self):
        print("A method")

class B:
    def methodB(self):
        print("B method")

class C(A, B):  # C inherits from both A and B
    pass

obj = C()
obj.methodA()  # From class A
obj.methodB()  # From class B


# =============================================================================
# MULTILEVEL INHERITANCE
# =============================================================================
"""
Child inherits from parent, which inherits from grandparent.
"""

print("\n" + "=" * 50)
print("MULTILEVEL INHERITANCE")
print("=" * 50)

class Grandparent:
    def method1(self):
        print("Grandparent method")

class Parent(Grandparent):
    def method2(self):
        print("Parent method")

class Child(Parent):
    def method3(self):
        print("Child method")

child = Child()
child.method1()  # From Grandparent
child.method2()  # From Parent
child.method3()  # Own method


# =============================================================================
# HIERARCHICAL INHERITANCE
# =============================================================================
"""
Multiple child classes inherit from one parent class.
"""

print("\n" + "=" * 50)
print("HIERARCHICAL INHERITANCE")
print("=" * 50)

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print(f"{self.brand} is starting...")

class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} car is driving")

class Motorcycle(Vehicle):
    def ride(self):
        print(f"{self.brand} motorcycle is riding")

car = Car("Toyota")
motorcycle = Motorcycle("Honda")

car.start()
car.drive()

print()
motorcycle.start()
motorcycle.ride()


# =============================================================================
# super() KEYWORD
# =============================================================================
"""
The super() keyword is used to access methods and constructors of a 
parent class from the child class.

Why Use super()?
- To reuse the parent class's methods or __init__() constructor
- Avoids hardcoding the parent class name
- Useful in inheritance (especially with multiple inheritance)
"""

print("\n" + "=" * 50)
print("super() KEYWORD")
print("=" * 50)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Call parent constructor
        self.student_id = student_id
        print(f"Student ID: {self.student_id}")

# Create object
s = Student("Mohsin", 20, "23-50194-1")


# =============================================================================
# METHOD OVERRIDING
# =============================================================================
"""
Child class can override (redefine) methods from the parent class.
"""

print("\n" + "=" * 50)
print("METHOD OVERRIDING")
print("=" * 50)

class Shape:
    def area(self):
        print("Calculating area...")
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):  # Override parent's area method
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):  # Override parent's area method
        return 3.14159 * self.radius ** 2

rect = Rectangle(10, 5)
circle = Circle(7)

print(f"Rectangle area: {rect.area()}")
print(f"Circle area: {circle.area():.2f}")


# =============================================================================
# CALLING PARENT METHOD WITH super()
# =============================================================================

print("\n" + "=" * 50)
print("CALLING PARENT METHOD WITH super()")
print("=" * 50)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # Call parent constructor
        self.department = department
    
    def display(self):
        super().display()  # Call parent's display method
        print(f"Department: {self.department}")

manager = Manager("Alice", 75000, "Engineering")
manager.display()
