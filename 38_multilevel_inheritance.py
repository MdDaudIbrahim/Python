"""
=============================================================================
                        MULTILEVEL INHERITANCE
=============================================================================

What is Multilevel Inheritance?
-------------------------------
Multilevel Inheritance means a class is derived from a class that is 
already derived from another class.

In simple words: Child → Parent → Grandparent

Syntax:
    class Grandparent:
        # code

    class Parent(Grandparent):
        # code

    class Child(Parent):
        # inherits from Parent (and indirectly Grandparent)

Key Points:
- Inherits features in a chain (like 3 generations)
- Child has access to all public members of Parent and Grandparent
- Helps build stepwise structure in OOP design

=============================================================================
"""


# =============================================================================
# BASIC MULTILEVEL INHERITANCE EXAMPLE
# =============================================================================

print("=" * 50)
print("MULTILEVEL INHERITANCE EXAMPLE")
print("=" * 50)

class Grandfather:
    def house(self):
        print("Grandfather: Owns a house")

class Father(Grandfather):
    def car(self):
        print("Father: Owns a car")

class Son(Father):
    def laptop(self):
        print("Son: Owns a laptop")

s = Son()
s.house()    # From Grandfather
s.car()      # From Father
s.laptop()   # From Son

"""
Output:
-------
Grandfather: Owns a house
Father: Owns a car
Son: Owns a laptop
"""


# =============================================================================
# ANOTHER MULTILEVEL INHERITANCE EXAMPLE
# =============================================================================

print("\n" + "=" * 50)
print("ANIMAL INHERITANCE CHAIN")
print("=" * 50)

class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating...")
    
    def sleep(self):
        print(f"{self.name} is sleeping...")

class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color
    
    def give_birth(self):
        print(f"{self.name} gives birth to live young")

class Dog(Mammal):
    def __init__(self, name, fur_color, breed):
        super().__init__(name, fur_color)
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says: Woof!")
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Fur Color: {self.fur_color}")
        print(f"Breed: {self.breed}")

# Create Dog object
dog = Dog("Buddy", "Golden", "Labrador")
dog.display_info()
print()
dog.eat()        # From Animal (grandparent)
dog.give_birth() # From Mammal (parent)
dog.bark()       # Own method


# =============================================================================
# MULTILEVEL WITH CONSTRUCTORS AND super()
# =============================================================================

print("\n" + "=" * 50)
print("VEHICLE INHERITANCE CHAIN")
print("=" * 50)

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        print(f"Vehicle created: {brand}")
    
    def start(self):
        print(f"{self.brand} is starting...")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
        print(f"Car model: {model}")
    
    def drive(self):
        print(f"{self.brand} {self.model} is driving...")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
        print(f"Battery: {battery_capacity} kWh")
    
    def charge(self):
        print(f"Charging {self.brand} {self.model}...")

print("Creating an Electric Car:")
tesla = ElectricCar("Tesla", "Model 3", 75)

print("\nUsing methods:")
tesla.start()   # From Vehicle (grandparent)
tesla.drive()   # From Car (parent)
tesla.charge()  # Own method


# =============================================================================
# FOUR-LEVEL INHERITANCE
# =============================================================================

print("\n" + "=" * 50)
print("FOUR-LEVEL INHERITANCE EXAMPLE")
print("=" * 50)

class LivingBeing:
    def breathe(self):
        print("Breathing...")

class Animal2(LivingBeing):
    def move(self):
        print("Moving...")

class Mammal2(Animal2):
    def feed_milk(self):
        print("Feeding milk to young...")

class Human(Mammal2):
    def speak(self):
        print("Speaking...")

human = Human()
human.breathe()    # From LivingBeing
human.move()       # From Animal2
human.feed_milk()  # From Mammal2
human.speak()      # Own method

# Show the inheritance chain
print(f"\nInheritance chain: {Human.__mro__}")


# =============================================================================
# PRACTICAL EXAMPLE - EMPLOYEE HIERARCHY
# =============================================================================

print("\n" + "=" * 50)
print("EMPLOYEE HIERARCHY EXAMPLE")
print("=" * 50)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, age, emp_id, salary, department, team_size):
        super().__init__(name, age, emp_id, salary)
        self.department = department
        self.team_size = team_size
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: ${self.salary}")
        print(f"Department: {self.department}")
        print(f"Team Size: {self.team_size}")

manager = Manager("Alice", 35, "M001", 85000, "Engineering", 10)
manager.display()
