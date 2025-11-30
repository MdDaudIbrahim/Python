"""
=============================================================================
                        ENCAPSULATION
=============================================================================

What is Encapsulation?
----------------------
Encapsulation is the OOP principle of hiding internal details and 
protecting object data from direct modification.

How It Works:
- Private attributes: Defined using underscore _ or double underscore __
- Accessed using getter and setter methods

Why Use Encapsulation?
- Prevents unauthorized access
- Makes the class modular and secure
- Allows validation before changing data

=============================================================================
"""


# =============================================================================
# BASIC ENCAPSULATION
# =============================================================================

print("=" * 50)
print("BASIC ENCAPSULATION")
print("=" * 50)

class Student:
    def __init__(self, name, age):
        self.__name = name   # private attribute (double underscore)
        self.__age = age

    def get_name(self):      # getter method
        return self.__name
    
    def set_name(self, name):  # setter method
        self.__name = name
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age > 0:          # Validation
            self.__age = age
        else:
            print("Age must be positive!")

# Create object
s1 = Student("Mohsin", 22)

print(f"Name: {s1.get_name()}")    # Access via getter

s1.set_name("Alif")                # Modify via setter
print(f"Name after update: {s1.get_name()}")

# Trying to access private attribute directly
# print(s1.__name)  # ❌ AttributeError!

# Validation in action
s1.set_age(-5)  # Will show error message
s1.set_age(25)  # Valid
print(f"Age: {s1.get_age()}")


# =============================================================================
# PROTECTED VS PRIVATE
# =============================================================================
"""
Naming Conventions:
- public      : name         (accessible everywhere)
- protected   : _name        (accessible within class and subclasses)
- private     : __name       (accessible only within class)
"""

print("\n" + "=" * 50)
print("PUBLIC, PROTECTED, AND PRIVATE")
print("=" * 50)

class Example:
    def __init__(self):
        self.public = "I am public"
        self._protected = "I am protected"
        self.__private = "I am private"
    
    def show_all(self):
        print(f"Public: {self.public}")
        print(f"Protected: {self._protected}")
        print(f"Private: {self.__private}")

obj = Example()

# Accessing from outside
print("Accessing from outside:")
print(f"  public: {obj.public}")           # ✅ Works
print(f"  _protected: {obj._protected}")   # ✅ Works (but not recommended)
# print(obj.__private)                     # ❌ AttributeError

print("\nAccessing from inside the class:")
obj.show_all()


# =============================================================================
# USING PROPERTY DECORATOR
# =============================================================================
"""
Python provides a cleaner way to implement getters and setters 
using the @property decorator.
"""

print("\n" + "=" * 50)
print("USING @property DECORATOR")
print("=" * 50)

class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance
    
    @property
    def balance(self):
        """Getter for balance"""
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        """Setter for balance with validation"""
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative!")
    
    @property
    def owner(self):
        return self.__owner
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive!")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: ${amount}")
        else:
            print("Invalid withdrawal amount!")

# Create account
account = BankAccount("Alice", 1000)

print(f"Owner: {account.owner}")
print(f"Balance: ${account.balance}")

# Use setter via property
account.balance = 1500
print(f"New Balance: ${account.balance}")

# Try invalid balance
account.balance = -100  # Will show error

# Deposit and withdraw
print()
account.deposit(500)
print(f"Balance after deposit: ${account.balance}")

account.withdraw(200)
print(f"Balance after withdrawal: ${account.balance}")
