'''
A lambda function, also known as an anonymous function or a lambda expression, is a concise way 
to create a function in programming without needing to define it using the usual syntax. Lambda
functions are typically used for short, simple operations where creating a named function would be 
excessive. They are often used as arguments to higher-order functions, allowing for more flexible and
expressive code.
'''
def func1():
    print('this message from func1')

lambda1 = lambda: print('this message from lambda1')

def func2(a):
    print('func2 ',a*a)

lambda2 = lambda a: print('lambda2 ',a*a)

def func3():
    return "this message from func3"

lambda3 = lambda : "this message from lambda3"

def func4(a):
    return a*a

lambda4 = lambda a: a*a

func1()
lambda1()
print('###############')

func2(4)
lambda2(4)
print('###############')

print(func3())
print(lambda3())
print('###############')

print(func4(5))
print(lambda4(5))
print('###############')


