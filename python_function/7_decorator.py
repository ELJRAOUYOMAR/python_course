'''
: Decorators are functions that modify the behavior of another function or method. 
They are often used to add functionality to existing functions without modifying their code directly.
'''
# sometimes called Meta programming
# every thing in python is object even functions
# Decorator take a function and add some functionality and return it
# decorator wrap other function and enhance their behaviour
# decorator is higher order function (function accept function as parameter)
 
def myDecorator(func):                    #decorator

    def nestefFunc():                     #any name, it's just for decoration  
        print('before')                   #message from decorator 
        func()
        print('after')                   #message from decorator 

    return nestefFunc                           #return all data

@myDecorator
def sayHey():
    print("Hello from {} function".format(sayHey.__name__))


@myDecorator
def sayHello():
    print("Hello from {} function".format(sayHello.__name__))


# call the functions
sayHey()
print('#'*30)
sayHello()