#declare function
def person(name, age, gender):
    print(f'name: {name}\nage: {age}\ngender:{gender}')

person('Ahmed',23,'Male')
print('############################')
person(name='Ahmed',gender='Male',age='23')