"""
=============================================================================
                        POLYMORPHISM
=============================================================================

What is Polymorphism?
---------------------
Polymorphism means "many forms" — the ability of different classes to 
respond to the same method in different ways.

It allows:
- Same method name to behave differently on different classes
- Flexibility in code design

Key Points:
- Allows same interface, different behavior
- Achieved via method overriding or common method names across classes
- Increases code reusability and scalability

=============================================================================
"""


# =============================================================================
# BASIC POLYMORPHISM EXAMPLE
# =============================================================================

print("=" * 50)
print("BASIC POLYMORPHISM EXAMPLE")
print("=" * 50)

class Cat:
    def sound(self):
        print("Cat: Meow")

class Dog:
    def sound(self):
        print("Dog: Woof")

# Polymorphism
def make_sound(animal):
    animal.sound()

c = Cat()
d = Dog()

make_sound(c)  # Cat: Meow
make_sound(d)  # Dog: Woof

"""
Output:
-------
Cat: Meow
Dog: Woof
"""


# =============================================================================
# POLYMORPHISM WITH INHERITANCE
# =============================================================================

print("\n" + "=" * 50)
print("POLYMORPHISM WITH INHERITANCE")
print("=" * 50)

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog: Woof!")

class Cat(Animal):
    def speak(self):
        print("Cat: Meow!")

class Cow(Animal):
    def speak(self):
        print("Cow: Moo!")

# List of different animals
animals = [Dog(), Cat(), Cow()]

# Same method call, different behavior
for animal in animals:
    animal.speak()


# =============================================================================
# POLYMORPHISM WITH FUNCTIONS
# =============================================================================

print("\n" + "=" * 50)
print("POLYMORPHISM WITH len() FUNCTION")
print("=" * 50)

# len() works on different data types - same function, different behavior

my_string = "Hello"
my_list = [1, 2, 3, 4, 5]
my_dict = {"a": 1, "b": 2, "c": 3}

print(f"len('{my_string}') = {len(my_string)}")  # String length
print(f"len({my_list}) = {len(my_list)}")         # List length
print(f"len({my_dict}) = {len(my_dict)}")         # Dictionary length


# =============================================================================
# POLYMORPHISM WITH OPERATORS
# =============================================================================

print("\n" + "=" * 50)
print("POLYMORPHISM WITH + OPERATOR")
print("=" * 50)

# + operator behaves differently based on operand types

num1, num2 = 10, 20
str1, str2 = "Hello", "World"
list1, list2 = [1, 2], [3, 4]

print(f"10 + 20 = {num1 + num2}")              # Addition
print(f"'Hello' + 'World' = '{str1 + str2}'") # Concatenation
print(f"[1, 2] + [3, 4] = {list1 + list2}")   # List concatenation


# =============================================================================
# METHOD OVERRIDING (RUNTIME POLYMORPHISM)
# =============================================================================

print("\n" + "=" * 50)
print("METHOD OVERRIDING")
print("=" * 50)

class Shape:
    def area(self):
        return 0
    
    def info(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):  # Override
        return self.width * self.height
    
    def info(self):  # Override
        print("I am a rectangle")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):  # Override
        return 3.14159 * self.radius ** 2
    
    def info(self):  # Override
        print("I am a circle")

shapes = [Rectangle(10, 5), Circle(7)]

for shape in shapes:
    shape.info()
    print(f"Area: {shape.area():.2f}\n")


# =============================================================================
# DUCK TYPING
# =============================================================================
"""
Duck Typing: "If it walks like a duck and quacks like a duck, it's a duck."

In Python, we don't check the type of object, we check if it has the 
required method/attribute.
"""

print("=" * 50)
print("DUCK TYPING")
print("=" * 50)

class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

class Fish:
    def swim(self):
        print("Fish is swimming")

def lift_off(entity):
    entity.fly()  # Works if entity has fly() method

bird = Bird()
airplane = Airplane()

lift_off(bird)      # Works - Bird has fly()
lift_off(airplane)  # Works - Airplane has fly()
# lift_off(Fish())  # ❌ Error - Fish doesn't have fly()


# =============================================================================
# PRACTICAL POLYMORPHISM EXAMPLE
# =============================================================================

print("\n" + "=" * 50)
print("PAYMENT SYSTEM EXAMPLE")
print("=" * 50)

class Payment:
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def __init__(self, card_number):
        self.card_number = card_number
    
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card ending in {self.card_number[-4:]}")

class PayPal(Payment):
    def __init__(self, email):
        self.email = email
    
    def pay(self, amount):
        print(f"Paid ${amount} using PayPal ({self.email})")

class Cash(Payment):
    def pay(self, amount):
        print(f"Paid ${amount} in Cash")

# Process payment - same interface, different behavior
def process_payment(payment_method, amount):
    payment_method.pay(amount)

# Different payment methods
cc = CreditCard("1234-5678-9012-3456")
pp = PayPal("user@email.com")
cash = Cash()

process_payment(cc, 100)
process_payment(pp, 50)
process_payment(cash, 25)
