"""
=============================================================================
                        CLASS METHODS
=============================================================================

What is a Class Method?
-----------------------
A class method is a method that works with the class itself, not the 
instance. It's defined using the @classmethod decorator, and it takes 
cls (class) as the first parameter.

Syntax:
    @classmethod
    def method_name(cls):
        # code

Key Points:
- Uses @classmethod decorator
- First argument is cls (refers to the class)
- Can access or modify class variables
- Can be called using class name or instance

=============================================================================
"""


# =============================================================================
# BASIC CLASS METHOD EXAMPLE
# =============================================================================

print("=" * 50)
print("BASIC CLASS METHOD EXAMPLE")
print("=" * 50)

class Student:
    University_name = "AIUB"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_University(cls, new_name):
        cls.University_name = new_name

# Before changing
print(Student.University_name)  # AIUB

# Using class method
Student.change_University("BUET")

# After changing
print(Student.University_name)  # BUET

"""
Output:
-------
AIUB
BUET
"""


# =============================================================================
# CLASS METHOD VS INSTANCE METHOD VS STATIC METHOD
# =============================================================================

print("\n" + "=" * 50)
print("COMPARISON: INSTANCE vs CLASS vs STATIC")
print("=" * 50)

class Employee:
    company = "TechCorp"  # Class variable
    employee_count = 0
    
    def __init__(self, name, salary):
        self.name = name        # Instance variable
        self.salary = salary
        Employee.employee_count += 1
    
    # Instance method - works with instance (self)
    def display(self):
        print(f"Name: {self.name}, Salary: ${self.salary}")
    
    # Class method - works with class (cls)
    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name
    
    @classmethod
    def get_employee_count(cls):
        return cls.employee_count
    
    # Static method - independent of class and instance
    @staticmethod
    def is_valid_salary(salary):
        return salary > 0

# Create employees
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

print(f"Company: {Employee.company}")
print(f"Total Employees: {Employee.get_employee_count()}")

# Change company name using class method
Employee.change_company("NewTech Inc.")
print(f"Company after change: {Employee.company}")

# Static method
print(f"Is -1000 valid salary? {Employee.is_valid_salary(-1000)}")


# =============================================================================
# CLASS METHOD AS ALTERNATIVE CONSTRUCTOR
# =============================================================================
"""
Class methods are often used to create alternative constructors - 
different ways to create objects.
"""

print("\n" + "=" * 50)
print("CLASS METHOD AS ALTERNATIVE CONSTRUCTOR")
print("=" * 50)

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    @classmethod
    def from_string(cls, date_string):
        """Create Date from string format: 'DD-MM-YYYY'"""
        day, month, year = map(int, date_string.split('-'))
        return cls(day, month, year)
    
    @classmethod
    def today(cls):
        """Create Date for today"""
        import datetime
        today = datetime.date.today()
        return cls(today.day, today.month, today.year)
    
    def display(self):
        print(f"{self.day:02d}/{self.month:02d}/{self.year}")

# Using regular constructor
date1 = Date(15, 8, 2023)
print("Using regular constructor:")
date1.display()

# Using class method (alternative constructor)
date2 = Date.from_string("25-12-2024")
print("\nUsing from_string():")
date2.display()

# Using today() class method
date3 = Date.today()
print("\nUsing today():")
date3.display()


# =============================================================================
# CLASS METHOD TO MODIFY CLASS STATE
# =============================================================================

print("\n" + "=" * 50)
print("MODIFYING CLASS STATE")
print("=" * 50)

class BankAccount:
    interest_rate = 0.05  # 5% interest rate (class variable)
    total_accounts = 0
    
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance
        BankAccount.total_accounts += 1
    
    def add_interest(self):
        self.balance += self.balance * BankAccount.interest_rate
    
    @classmethod
    def set_interest_rate(cls, new_rate):
        """Change interest rate for all accounts"""
        cls.interest_rate = new_rate
        print(f"Interest rate changed to {new_rate * 100}%")
    
    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

# Create accounts
acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 2000)

print(f"Total accounts: {BankAccount.get_total_accounts()}")
print(f"Current interest rate: {BankAccount.interest_rate * 100}%")

# Add interest to acc1
acc1.add_interest()
print(f"Alice's balance after interest: ${acc1.balance}")

# Change interest rate for all accounts
BankAccount.set_interest_rate(0.07)

# Add interest to acc2 (uses new rate)
acc2.add_interest()
print(f"Bob's balance after interest: ${acc2.balance}")


# =============================================================================
# CLASS METHOD WITH INHERITANCE
# =============================================================================

print("\n" + "=" * 50)
print("CLASS METHOD WITH INHERITANCE")
print("=" * 50)

class Animal:
    species_count = 0
    
    def __init__(self, name):
        self.name = name
        Animal.species_count += 1
    
    @classmethod
    def get_species_count(cls):
        return cls.species_count
    
    @classmethod
    def create_anonymous(cls):
        """Factory method to create animal without name"""
        return cls("Unknown")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} says: Meow!")

# Create using class method
dog1 = Dog.create_anonymous()  # Returns a Dog object
cat1 = Cat.create_anonymous()  # Returns a Cat object

dog1.bark()
cat1.meow()

print(f"\nTotal animals created: {Animal.get_species_count()}")
