"""
=============================================================================
                        MULTIPLE INHERITANCE
=============================================================================

What is Multiple Inheritance?
-----------------------------
Multiple Inheritance is when a child class inherits from more than one 
parent class.

Syntax:
    class Parent1:
        # code

    class Parent2:
        # code

    class Child(Parent1, Parent2):
        # inherits from both Parent1 and Parent2

Key Points:
- Child class gets properties from multiple parent classes
- Python uses Method Resolution Order (MRO) to decide which method 
  to use if there's a conflict
- Helps combine features from multiple sources

=============================================================================
"""


# =============================================================================
# BASIC MULTIPLE INHERITANCE EXAMPLE
# =============================================================================

print("=" * 50)
print("MULTIPLE INHERITANCE EXAMPLE")
print("=" * 50)

class Father:
    def skill(self):
        print("Father: Farming")

class Mother:
    def talent(self):
        print("Mother: Cooking")

class Child(Father, Mother):  # Multiple Inheritance
    def hobby(self):
        print("Child: Drawing")

c = Child()
c.skill()     # Inherited from Father
c.talent()    # Inherited from Mother
c.hobby()     # Own method

"""
Output:
-------
Father: Farming
Mother: Cooking
Child: Drawing
"""


# =============================================================================
# ANOTHER MULTIPLE INHERITANCE EXAMPLE
# =============================================================================

print("\n" + "=" * 50)
print("FLYING FISH EXAMPLE")
print("=" * 50)

class Fish:
    def swim(self):
        print("I can swim!")
    
    def habitat(self):
        print("I live in water")

class Bird:
    def fly(self):
        print("I can fly!")
    
    def habitat(self):
        print("I live in the sky")

class FlyingFish(Fish, Bird):  # Inherits from both
    def display(self):
        print("I am a Flying Fish!")

ff = FlyingFish()
ff.display()
ff.swim()    # From Fish
ff.fly()     # From Bird
ff.habitat() # From Fish (first parent in MRO)


# =============================================================================
# METHOD RESOLUTION ORDER (MRO)
# =============================================================================
"""
When multiple parent classes have the same method, Python uses MRO
to determine which method to call.

MRO follows the order in which classes are listed in inheritance.
"""

print("\n" + "=" * 50)
print("METHOD RESOLUTION ORDER (MRO)")
print("=" * 50)

class A:
    def show(self):
        print("Method from class A")

class B:
    def show(self):
        print("Method from class B")

class C(A, B):
    pass

class D(B, A):
    pass

c = C()
d = D()

print("C inherits from (A, B):")
c.show()  # Uses A's method (first in order)

print("\nD inherits from (B, A):")
d.show()  # Uses B's method (first in order)

# View MRO
print(f"\nMRO of C: {C.__mro__}")
print(f"MRO of D: {D.__mro__}")


# =============================================================================
# MULTIPLE INHERITANCE WITH CONSTRUCTORS
# =============================================================================

print("\n" + "=" * 50)
print("MULTIPLE INHERITANCE WITH CONSTRUCTORS")
print("=" * 50)

class Engine:
    def __init__(self):
        self.engine_type = "V8"
        print("Engine initialized")
    
    def start_engine(self):
        print(f"{self.engine_type} engine started!")

class Wheels:
    def __init__(self):
        self.num_wheels = 4
        print("Wheels initialized")
    
    def rotate(self):
        print(f"{self.num_wheels} wheels rotating!")

class Car(Engine, Wheels):
    def __init__(self):
        Engine.__init__(self)  # Explicitly call Engine's __init__
        Wheels.__init__(self)  # Explicitly call Wheels' __init__
        self.brand = "Toyota"
        print("Car initialized")
    
    def drive(self):
        print(f"{self.brand} is driving!")

print("Creating a Car:")
car = Car()
print()
car.start_engine()
car.rotate()
car.drive()


# =============================================================================
# PRACTICAL EXAMPLE - SMART DEVICE
# =============================================================================

print("\n" + "=" * 50)
print("SMART DEVICE EXAMPLE")
print("=" * 50)

class Phone:
    def call(self):
        print("Making a phone call...")
    
    def send_message(self):
        print("Sending a message...")

class Camera:
    def take_photo(self):
        print("Taking a photo...")
    
    def record_video(self):
        print("Recording video...")

class SmartPhone(Phone, Camera):
    def browse_internet(self):
        print("Browsing the internet...")

phone = SmartPhone()
phone.call()           # From Phone
phone.take_photo()     # From Camera
phone.browse_internet() # Own method
