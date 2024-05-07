# serialize => convert a class object to json
# 1. Import the json module 
# 2. Create instance in your class
# 3. Use json.dumps() function to convert a class object to json-formatted string

# 1 
import json

class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
# 2
my_object = MyClass("Ahmed", 19)

# 3
json_string = json.dumps(my_object.__dict__)

print(json_string)
print(type(json_string))