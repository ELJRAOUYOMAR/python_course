def myDecorator(func):
    def nestedFunc(*args, **kwargs):
        print('before')
        print("Hello from {} function".format(func.__name__))
        func(*args, **kwargs)
        print('after')
    return nestedFunc

@myDecorator
def sayHey():
    pass

@myDecorator
def sayHello():
    pass

# Call the functions
sayHey()
print('#'*30)
sayHello()
