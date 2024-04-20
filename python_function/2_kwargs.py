''' *args: This syntax allows you to pass a variable number of positional arguments to a function.
The *args parameter collects all the positional arguments passed to the function into a tuple. '''

''' **kwargs: This syntax allows you to pass a variable number of 
keyword arguments (i.e., arguments preceded by a named keyword) to a function.
The **kwargs parameter collects these arguments into a dictionary,
where the keys are the argument names and the values are the corresponding values. '''


def person(**kwargs):
    print(kwargs)

def person2(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}={value}")

def person3(**kwargs):
    print('name=',kwargs.get('name'))
    print('age=',kwargs["age"])
    print('phone=',kwargs.get('phone'))

def person4(*args):
    print(args[0])
    print(args[1])
    print(args[3])

print('#### person1 ###')
person(name="Ahmed",age=26,gender='female',phone='+9 87766898789')
print('\n#### person2 ###')
person2(name="Ahmed",age=26,gender='female',phone='+9 87766898789')
print('\n#### person3 ###')
person3(name='ahmed',phone='+9 8798798',gender='male',age=26)
print('\n#### person4 ###')
person4('ahmed','+9 8798798','male',26)
