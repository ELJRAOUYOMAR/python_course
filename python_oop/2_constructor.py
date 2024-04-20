'''
Constructor:

-Special method (__init__) in a class.
-Automatically initializes object attributes.
-Invoked upon object creation.
-Differs from normal class methods by its automatic invocation and role in object initialization.
-the difference between constructor and normal function is constructor is execut when creating a new instance, 
but the function should called it
'''

class Person:
    # class variable
    name = "Yasser"
    def __init__(self):
        # instance variable
        # name = 'yasser'
        print("Hello from", self.name)

sayHello  = Person()

print('*'*30)

# example 2 with parametares in constructor
class Home:
    def __init__(self, location):
        print(location)
    
my_home = Home("Africa")
