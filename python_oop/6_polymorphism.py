
'''
Polymorphism refers to the ability of different objects to respond to the same message (method call)
in different ways. There are two main types of polymorphism: 
compile-time polymorphism (method overloading) and 
runtime polymorphism (method overriding).
'''

# Example 0
class A:
    def do_something(self):
        print("From class A")

        raise NotImplementedError("Derived class must implement do_something method")

class B(A):
    def do_something(self):
        print("From class B")

class C(A):
    def do_something(self):
        # print("From class C")
        pass 

b = B()
c = C()

b.do_something()
c.do_something()

# Example1
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Bird(Animal):
    def make_sound(self):
        return "Tweet!"

# Function to demonstrate polymorphism
def animal_sound(animal):
    return animal.make_sound()

# Creating instances of different animals
dog = Dog("Dog")
cat = Cat("Cat")
bird = Bird("Bird")

# Calling the function with different animal instances
print(animal_sound(dog))  # Output: Woof!
print(animal_sound(cat))  # Output: Meow!
print(animal_sound(bird))  # Output: Chirp!

# Example 2
class Vehicle:
    def drive(self):
        raise NotImplementedError("Subclasses must implement the drive method")

class Car(Vehicle):
    def drive(self):
        return "Driving a car"

class Bicycle(Vehicle):
    # The drive method is not implemented for Bicycle
    pass

car = Car()
print(car.drive())  # Output: Driving a car

bicycle = Bicycle()
# Calling drive on Bicycle will raise NotImplementedError
# because it hasn't been implemented in the subclass
bicycle.drive()  # Output: NotImplementedError: Subclasses must implement the drive method
