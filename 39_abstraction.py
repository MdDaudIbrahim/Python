"""
=============================================================================
                        ABSTRACTION
=============================================================================

What is Abstraction?
--------------------
Abstraction means hiding the internal implementation and showing only 
essential features to the user.

In Python, abstraction is achieved using:
- Abstract classes
- Abstract methods
- Done using the abc module (abc = Abstract Base Class)

Syntax:
    from abc import ABC, abstractmethod

    class MyAbstractClass(ABC):
        @abstractmethod
        def abstract_method(self):
            pass

Key Points:
- Abstract class cannot be instantiated (can't create object directly)
- All child classes must override the abstract methods
- Encourages design consistency
- Promotes security and cleaner code

=============================================================================
"""


# =============================================================================
# BASIC ABSTRACTION EXAMPLE
# =============================================================================

from abc import ABC, abstractmethod

print("=" * 50)
print("BASIC ABSTRACTION EXAMPLE")
print("=" * 50)

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog: Woof!")

class Cat(Animal):
    def sound(self):
        print("Cat: Meow!")

# a = Animal()  # ❌ Cannot create object of abstract class
d = Dog()
d.sound()

c = Cat()
c.sound()

"""
Output:
-------
Dog: Woof!
Cat: Meow!
"""


# =============================================================================
# ABSTRACT CLASS WITH REGULAR METHODS
# =============================================================================
"""
Abstract classes can have both abstract methods (must be overridden)
and regular methods (can be inherited as-is).
"""

print("\n" + "=" * 50)
print("ABSTRACT CLASS WITH REGULAR METHODS")
print("=" * 50)

class Shape(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def area(self):
        """Must be implemented by child classes"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Must be implemented by child classes"""
        pass
    
    def display_name(self):
        """Regular method - can be inherited"""
        print(f"Shape: {self.name}")


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius


rect = Rectangle(10, 5)
rect.display_name()  # Inherited regular method
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")

print()

circle = Circle(7)
circle.display_name()  # Inherited regular method
print(f"Area: {circle.area():.2f}")
print(f"Perimeter: {circle.perimeter():.2f}")


# =============================================================================
# MULTIPLE ABSTRACT METHODS
# =============================================================================

print("\n" + "=" * 50)
print("VEHICLE ABSTRACTION EXAMPLE")
print("=" * 50)

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
    @abstractmethod
    def fuel_type(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car: Turning the key, engine starts")
    
    def stop(self):
        print("Car: Pressing brake, engine stops")
    
    def fuel_type(self):
        return "Petrol/Diesel"


class ElectricBike(Vehicle):
    def start(self):
        print("E-Bike: Press power button, motor activates")
    
    def stop(self):
        print("E-Bike: Release throttle, apply brakes")
    
    def fuel_type(self):
        return "Electric"


car = Car()
car.start()
car.stop()
print(f"Fuel: {car.fuel_type()}")

print()

ebike = ElectricBike()
ebike.start()
ebike.stop()
print(f"Fuel: {ebike.fuel_type()}")


# =============================================================================
# ABSTRACT PROPERTIES
# =============================================================================

print("\n" + "=" * 50)
print("ABSTRACT PROPERTIES")
print("=" * 50)

class Employee(ABC):
    @property
    @abstractmethod
    def salary(self):
        pass
    
    @abstractmethod
    def work(self):
        pass


class Developer(Employee):
    def __init__(self, name, base_salary):
        self.name = name
        self._salary = base_salary
    
    @property
    def salary(self):
        return self._salary
    
    def work(self):
        print(f"{self.name} is writing code...")


class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        self.name = name
        self._salary = base_salary + bonus
    
    @property
    def salary(self):
        return self._salary
    
    def work(self):
        print(f"{self.name} is managing the team...")


dev = Developer("Alice", 70000)
dev.work()
print(f"Salary: ${dev.salary}")

print()

mgr = Manager("Bob", 80000, 15000)
mgr.work()
print(f"Salary: ${mgr.salary}")


# =============================================================================
# WHY USE ABSTRACTION?
# =============================================================================

print("\n" + "=" * 50)
print("BENEFITS OF ABSTRACTION")
print("=" * 50)

print("""
1. DESIGN CONSISTENCY
   - Forces all subclasses to implement required methods
   - Ensures uniform interface across different implementations

2. CODE ORGANIZATION
   - Separates "what" from "how"
   - Abstract class defines WHAT to do
   - Concrete classes define HOW to do it

3. SECURITY
   - Hides complex implementation details
   - Users only see essential features

4. FLEXIBILITY
   - Easy to add new implementations
   - Changes in one class don't affect others

5. MAINTAINABILITY
   - Clear structure makes code easier to understand
   - Easier to debug and modify
""")
