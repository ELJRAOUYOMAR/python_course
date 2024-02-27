'''
A Higher-Order Function (HOF) is a function that either takes one or more functions as arguments
or returns a function as its result. In other words, it treats functions as first-class citizens,
allowing them to be manipulated and passed around like any other data type. Higher-order functions 
enable functional programming paradigms such as function composition, partial application, 
and abstraction of control flow.
'''
def sum1(a,b):
    print("sum of {} and {} is {}".format(a,b,a+b))

sum2 = lambda a,b: print("sum of {} and {} is {}".format(a,b,a+b))

def hof(x,y,z):
    z(x,y)

hof(3,2,sum1)
print('########')
hof(3,2,sum2)