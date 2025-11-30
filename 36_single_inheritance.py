"""
=============================================================================
                        SINGLE INHERITANCE
=============================================================================

What is Single Inheritance?
---------------------------
Single Inheritance is when a child class inherits from only one parent class.

Syntax:
    class Parent:
        # parent class content

    class Child(Parent):
        # inherits from Parent

Key Points:
- Promotes code reusability
- Only one parent class
- The child can use all non-private members of the parent

=============================================================================
"""


# =============================================================================
# BASIC SINGLE INHERITANCE EXAMPLE
# =============================================================================

print("=" * 50)
print("SINGLE INHERITANCE EXAMPLE")
print("=" * 50)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id


# Create object
s1 = Student("Mohsin", 22, "23-50194-1")
print(s1.name)
print(s1.age)
print(s1.student_id)

print()

s2 = Student("Jam", 20, "23-50187-1")
print(s2.name)
print(s2.age)
print(s2.student_id)

"""
Output:
-------
Mohsin
22
23-50194-1

Jam
20
23-50187-1
"""


# =============================================================================
# ANOTHER SINGLE INHERITANCE EXAMPLE
# =============================================================================

print("\n" + "=" * 50)
print("EMPLOYEE INHERITANCE EXAMPLE")
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
        super().display()  # Call parent method
        print(f"Department: {self.department}")


# Create Manager object
m1 = Manager("Alice", 75000, "Engineering")
m1.display()


# =============================================================================
# INHERITANCE WITH ADDITIONAL METHODS
# =============================================================================

print("\n" + "=" * 50)
print("VEHICLE INHERITANCE EXAMPLE")
print("=" * 50)

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start(self):
        print(f"{self.brand} {self.model} is starting...")
    
    def stop(self):
        print(f"{self.brand} {self.model} has stopped.")


class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors
    
    def honk(self):
        print("Beep beep!")
    
    def display_info(self):
        print(f"Car: {self.brand} {self.model}")
        print(f"Doors: {self.num_doors}")


# Create Car object
my_car = Car("Toyota", "Camry", 4)
my_car.display_info()
my_car.start()      # Inherited from Vehicle
my_car.honk()       # Own method
my_car.stop()       # Inherited from Vehicle
