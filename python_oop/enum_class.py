'''
An enum (short for "enumeration") in Python is a data type that consists of a set of predefined values.
Each value in an enum is typically assigned a name, making code more readable and maintainable by 
providing meaningful labels for constants.
'''

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)        # Output: Color.RED
print(Color.RED.value)  # Output: 1
print(Color.GREEN.name) # Output: GREEN

print("'"*40)

for i in Color:
    print(repr(i))