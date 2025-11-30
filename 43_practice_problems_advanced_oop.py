"""
=============================================================================
            PRACTICE PROBLEMS - ADVANCED OOP
=============================================================================

This file contains practice problems covering:
- Classes and Objects
- Encapsulation
- Inheritance
- Polymorphism
- super() function

=============================================================================
"""


# =============================================================================
# PROBLEM 1: Bank Account System
# =============================================================================
"""
Write a Python program to define a class named BankAccount that models 
a simple bank account with:

Attributes:
- name (the name of the account holder)
- balance (the current account balance)

Methods:
- deposit(amount) – adds the specified amount to the balance
- withdraw(amount) – deducts the amount if sufficient funds available
- display_balance() – displays the current balance
"""

print("=" * 50)
print("PROBLEM 1: Bank Account System")
print("=" * 50)

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} BDT deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} BDT withdrawn successfully.")
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: {self.balance} BDT")

# Example usage
account1 = BankAccount("Mohsin", 10000)

account1.display_balance()
account1.deposit(2000)
account1.withdraw(5000)
account1.display_balance()

"""
Output:
-------
Account Holder: Mohsin
Current Balance: 10000 BDT
2000 BDT deposited successfully.
5000 BDT withdrawn successfully.
Account Holder: Mohsin
Current Balance: 7000 BDT
"""


# =============================================================================
# PROBLEM 2: Shape Inheritance and Polymorphism
# =============================================================================
"""
Write a Python program to implement inheritance using OOP:
- Create a base class Shape with a method area() that returns 0
- Derive subclasses: Square, Circle, Triangle
- Override the area() method in each subclass
- Demonstrate polymorphism by calling area() for each shape
"""

print("\n" + "=" * 50)
print("PROBLEM 2: Shape Inheritance and Polymorphism")
print("=" * 50)

import math

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Create a list of different shapes
shapes = [Square(4), Circle(5), Triangle(6, 5)]

# Loop through each shape and print its name and area
print("Shape Areas:\n" + "-" * 20)
for shape in shapes:
    name = shape.__class__.__name__  # Get the class name
    area = shape.area()               # Call the area method
    print(f"{name} area: {area:.2f}")

"""
Output:
-------
Shape Areas:
--------------------
Square area: 16.00
Circle area: 78.54
Triangle area: 15.00
"""


# =============================================================================
# PROBLEM 3: Inheritance with super()
# =============================================================================
"""
Write a Python program to demonstrate inheritance and super():
- Create a base class Person with attributes name and age
- Create a derived class Employee with salary and department attributes
- Use super() to initialize base class attributes
- Display the details of the employee
"""

print("\n" + "=" * 50)
print("PROBLEM 3: Inheritance with super()")
print("=" * 50)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age)
        self.salary = salary
        self.department = department

    def display(self):
        super().display()
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")

# Example usage
emp1 = Employee("Alif Hasan Khan", 25, 50000, "IT")
emp1.display()

print("-" * 20)

emp2 = Employee("Mohsin Ibna Hossain", 27, 70000, "IT")
emp2.display()

"""
Output:
-------
Name: Alif Hasan Khan
Age: 25
Salary: 50000
Department: IT
--------------------
Name: Mohsin Ibna Hossain
Age: 27
Salary: 70000
Department: IT
"""


# =============================================================================
# PROBLEM 4: Movie Ticket Booking System
# =============================================================================
"""
Design a Movie Ticket Booking System using OOP:
- Create base class Ticket with: _price (private), seat_no
- Include methods: get_price, set_price, display_info
- Create derived class StudentTicket with discount
- Demonstrate encapsulation and super()
"""

print("\n" + "=" * 50)
print("PROBLEM 4: Movie Ticket Booking System")
print("=" * 50)

class Ticket:
    def __init__(self, price, seat_no):
        self._price = price    # Encapsulated (private) attribute
        self.seat_no = seat_no

    def get_price(self):
        return self._price

    def set_price(self, price):
        if price >= 0:
            self._price = price
        else:
            print("Invalid price!")

    def display_info(self):
        print(f"Seat No: {self.seat_no}")
        print(f"Ticket Price: BDT {self._price}")

class StudentTicket(Ticket):
    def __init__(self, price, seat_no, discount):
        super().__init__(price, seat_no)
        self.discount = discount

    def apply_discount(self):
        discounted_price = self.get_price() * (1 - self.discount / 100)
        self.set_price(discounted_price)

    def display_info(self):
        self.apply_discount()
        print("Student Ticket Info:")
        super().display_info()

ticket1 = StudentTicket(500, "A12", 20)
ticket1.display_info()

print()

# Regular ticket
ticket2 = Ticket(500, "B15")
print("Regular Ticket Info:")
ticket2.display_info()

"""
Output:
-------
Student Ticket Info:
Seat No: A12
Ticket Price: BDT 400.0

Regular Ticket Info:
Seat No: B15
Ticket Price: BDT 500
"""
