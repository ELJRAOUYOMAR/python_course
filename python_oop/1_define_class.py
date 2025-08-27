'''
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of objects, 
which can contain data and code. It focuses on modularizing code into reusable components and emphasizes
concepts like encapsulation, inheritance, and polymorphism.
'''

'''
In Python, attributes are created when the object is instantiated, so while we can delete 
attributes within the class definition, they remain accessible when accessed through an instance
of the class.
'''
'''
In Python, self is a conventional name used to refer to the instance of the class within its methods.
It allows methods to access and modify the attributes and methods of the current object. 
Essentially, self is a reference to the object itself, enabling it to interact with its own data and
behavior.
'''

class Person:
    # name = ""
    # age = 0

    def info(self):
        return f"name of the class :{self.__class__.__name__}\nname: {self.name}\nage: {self.age}\n"
    
class Person2:
    def __init__(self, name):
        self.name = name
    
    def info(self):
        print(f"name of the person 2: {self.name}\n")

class Car:
    def info(self, module, color):
        self.module = module
        self.color = color

        return f"{self.__class__.__name__}\nmodule: {self.module}\ncolor: {self.color}\n"


# create object (instance from class Person)
person1 = Person()

person1.name = "Alice"
person1.age = 13
print(person1.info())

# pass the name as constructor using the method init
Person2("Mohamed").info()

audi = Car()
infos = audi.info("audi","black")
print(infos)