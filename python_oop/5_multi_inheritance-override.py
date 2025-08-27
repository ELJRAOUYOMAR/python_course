'''
In object-oriented programming (OOP), "override" refers to the ability to provide a new 
implementation for a method that is already defined in a superclass (or parent class) within
 a subclass (or child class). When you override a method, you're essentially replacing the inherited
   implementation with a new one that is specific to the subclass.
'''

class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print("hello")
        pass  # Placeholder method, to be overridden by subclasses

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        super().make_sound()
        return "Meow!"

class Bird(Animal):
    def make_sound(self):
        return "Tweet!"

# Creating instances of each class
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweetie")

# Using the methods of the instances
print(cat.name + " says: " + cat.make_sound())
# bacause the make_sound overrided, so here just the make_sound() of child(subclass) will executs
print(dog.name + " says: " + dog.make_sound())
# also here
print(bird.name + " says: " + bird.make_sound())
