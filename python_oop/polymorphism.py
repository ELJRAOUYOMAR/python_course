"""
Polymorphism in Python refers to the ability of different classes to be treated as objects of a 
common superclass. It allows methods to behave differently based on the object that they are called on.
This enables code flexibility and reusability, as a single method can be used with various types of 
objects, adapting its behavior accordingly.
"""

class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

class Bird(Animal):
    def sound(self):
        return "Tweet!"


class Anything():
    # pass dog as argument
    def any_sound(self, animal: Animal):
        print(animal.sound())

# create instance of Dog class
dog_obj = Anything()

# even we pass the parent class as argument we can make an object of childs and print the function(sound), that's the polymorphism
dog_sound = dog_obj.any_sound(Dog())
# print(dog_sound)

print("#"*30)

# Function that demonstrates polymorphism
# it takes argument not integer, not string...but Animal class, so when we declare it, we should pass an object of the class Animal as parameter  
# we can write just without declare the type def make_sound(animal):, this just for clarifay 
def make_sound(animal: Animal):
    return animal.sound()

# Creating instances of each class
dog = Dog()
cat = Cat()
bird = Bird()

# Using the make_sound function with different objects
print("Dog says:", make_sound(dog))
print("Cat says:", make_sound(cat))
print("Bird says:", make_sound(bird))
