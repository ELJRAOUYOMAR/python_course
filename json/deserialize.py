# deserialize(convert json to class object)

import json

class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# json data (in string format) 
json_data = '{"name": "Ahmed", "age": 27}'

# deserialize json data to python dictionary
data_dict = json.loads(json_data)

# create an instance of MyClass using the dictionary data
# the double asterisk(**) is used for dictionary unpacking in python 
''' It allows you to take a dictionary and "unpack" its key-value pairs as keyword arguments when 
calling a function or creating an instance of a class'''
my_object = MyClass(**data_dict)

print(my_object)
print(my_object.name)
print(my_object.age)
print(my_object.__dict__)
