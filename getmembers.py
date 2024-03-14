import inspect

def get_module_properties(module):
    properties = {}
    for name, obj in inspect.getmembers(module):
        if not name.startswith("__"):  # Exclude private and special methods
            properties[name] = obj
    return properties

# Example usage:
import math
import sys
module_properties = get_module_properties(sys)
for name, obj in module_properties.items():
    print(f"{name}: {obj}")