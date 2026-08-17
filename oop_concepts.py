"""
Python OOP Concepts - Complete Guide
====================================

1. Class & Object
2. Encapsulation
3. Inheritance
4. Polymorphism
5. Abstraction
"""

from abc import ABC, abstractmethod

# =============================================================================
# 1. CLASS & OBJECT
# =============================================================================
# A class is a blueprint. An object is an actual thing built from that
# blueprint.


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")


# Creating objects (instances) from the class
dog1 = Dog("Rex", "Labrador")
dog2 = Dog("Bella", "Poodle")

dog1.bark()  # Rex says Woof!
dog2.bark()  # Bella says Woof!

# __init__ is the constructor — runs automatically when you create an object.
# self refers to the specific object being worked with.


# =============================================================================
# 2. ENCAPSULATION
# =============================================================================
# Bundling data (attributes) and methods together, and restricting
# direct access to some of it.


class BankAccount:
    def __init__(self, balance):
        # double underscore = "private" (name-mangled)
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500

# print(account.__balance)  # ❌ AttributeError — can't access directly

# __balance is hidden from outside code. You're forced to go through
# deposit() and get_balance(), which protects the data from being
# changed carelessly.


# =============================================================================
# 3. INHERITANCE
# =============================================================================
# A class can reuse and extend another class's behavior.


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


class Cat(Animal):  # Cat inherits from Animal
    def speak(self):  # overriding the parent method
        print(f"{self.name} says Meow")


class Bird(Animal):
    pass  # inherits speak() as-is, no changes


cat = Cat("Whiskers")
bird = Bird("Tweety")

cat.speak()  # Whiskers says Meow
bird.speak()  # Tweety makes a sound

# Cat and Bird are subclasses of Animal (the parent/base class).
# They automatically get __init__ and speak(), but Cat overrides
# speak() with its own version.


# =============================================================================
# 4. POLYMORPHISM
# =============================================================================
# Different classes respond to the same method call in their own way.

animals = [Cat("Milo"), Bird("Sunny"), Animal("Generic")]

for animal in animals:
    animal.speak()  # Each object responds differently, same method name

# Output:
# Milo says Meow
# Sunny makes a sound
# Generic makes a sound

# You call .speak() the same way on every object, but each one
# behaves according to its own class.


# =============================================================================
# 5. ABSTRACTION
# =============================================================================
# Hiding complex implementation details behind a simple interface,
# often using abstract classes.


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # no implementation — subclasses MUST provide one


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius**2


# shape = Shape()  # ❌ Error - can't instantiate an abstract class

rect = Rectangle(4, 5)
circle = Circle(3)
print(rect.area())  # 20
print(circle.area())  # 28.27...
