"""
=============================================================================
                PRACTICE PROBLEMS - OOP
=============================================================================

This file contains practice problems to help you understand 
Object-Oriented Programming in Python.

=============================================================================
"""


# =============================================================================
# PROBLEM 1: Create a Simple Class
# =============================================================================
"""
Create a class called 'Book' with attributes: title, author, and pages.
Add a method to display book information.
"""

print("=" * 50)
print("PROBLEM 1: Create a Simple Class")
print("=" * 50)

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

book1 = Book("Python Programming", "John Smith", 450)
book2 = Book("Data Science Basics", "Jane Doe", 380)

print("Book 1:")
book1.display_info()

print("\nBook 2:")
book2.display_info()


# =============================================================================
# PROBLEM 2: Bank Account with Encapsulation
# =============================================================================
"""
Create a BankAccount class with private balance.
Implement deposit, withdraw, and check balance methods.
"""

print("\n" + "=" * 50)
print("PROBLEM 2: Bank Account with Encapsulation")
print("=" * 50)

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.__account_holder = account_holder
        self.__balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Invalid deposit amount!")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: ${amount}")
        else:
            print("Invalid withdrawal or insufficient funds!")
    
    def check_balance(self):
        print(f"Account Holder: {self.__account_holder}")
        print(f"Current Balance: ${self.__balance}")

account = BankAccount("Mohsin", 1000)
account.check_balance()

print()
account.deposit(500)
account.withdraw(200)
account.check_balance()


# =============================================================================
# PROBLEM 3: Inheritance - Employee System
# =============================================================================
"""
Create an Employee base class and Manager/Developer child classes.
"""

print("\n" + "=" * 50)
print("PROBLEM 3: Inheritance - Employee System")
print("=" * 50)

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.emp_id}")
        print(f"Salary: ${self.salary}")

class Manager(Employee):
    def __init__(self, name, emp_id, salary, team_size):
        super().__init__(name, emp_id, salary)
        self.team_size = team_size
    
    def display(self):
        super().display()
        print(f"Team Size: {self.team_size}")

class Developer(Employee):
    def __init__(self, name, emp_id, salary, programming_language):
        super().__init__(name, emp_id, salary)
        self.programming_language = programming_language
    
    def display(self):
        super().display()
        print(f"Language: {self.programming_language}")

manager = Manager("Alice", "M001", 80000, 10)
developer = Developer("Bob", "D001", 65000, "Python")

print("Manager:")
manager.display()

print("\nDeveloper:")
developer.display()


# =============================================================================
# PROBLEM 4: Shape Classes with Method Overriding
# =============================================================================
"""
Create Shape, Rectangle, Circle, and Triangle classes.
Override the area() method in each child class.
"""

print("\n" + "=" * 50)
print("PROBLEM 4: Shape Classes")
print("=" * 50)

class Shape:
    def area(self):
        return 0
    
    def perimeter(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

rect = Rectangle(10, 5)
circle = Circle(7)
triangle = Triangle(6, 4, 5, 5, 6)

print(f"Rectangle - Area: {rect.area()}, Perimeter: {rect.perimeter()}")
print(f"Circle - Area: {circle.area():.2f}, Perimeter: {circle.perimeter():.2f}")
print(f"Triangle - Area: {triangle.area()}, Perimeter: {triangle.perimeter()}")


# =============================================================================
# PROBLEM 5: Student Grade System
# =============================================================================
"""
Create a Student class that stores name, subjects, and marks.
Calculate average and determine grade.
"""

print("\n" + "=" * 50)
print("PROBLEM 5: Student Grade System")
print("=" * 50)

class StudentGrade:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.marks = {}
    
    def add_subject(self, subject, mark):
        self.marks[subject] = mark
    
    def calculate_average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks.values()) / len(self.marks)
    
    def get_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    
    def display_report(self):
        print(f"\nStudent: {self.name} (ID: {self.student_id})")
        print("-" * 30)
        for subject, mark in self.marks.items():
            print(f"  {subject}: {mark}")
        print("-" * 30)
        print(f"  Average: {self.calculate_average():.2f}")
        print(f"  Grade: {self.get_grade()}")

student = StudentGrade("Mohsin", "23-50194-1")
student.add_subject("Math", 85)
student.add_subject("Physics", 78)
student.add_subject("Programming", 92)
student.add_subject("English", 88)

student.display_report()
