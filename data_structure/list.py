''' creating lists in python in different ways'''

simpleList = ["morocco", "Egypt", "Palestine"]
print(f'simple list = {simpleList}')

# using list() constructor
digits = list(range(10))
print(f"using list() = {digits}")

# using list comprehension
odd_numbers = [number for number in range(1, 10) if number % 2 == 0]
print(f'odd numbers: {odd_numbers}')

# using split 
string_not_splitted = "morocco, egypt, palestine"
list_from_string = string_not_splitted.split(",")
print(f"list from split(){list_from_string}")

# using the * opearator
repeated_list = [0] * 4
print(f'list using * operator: {repeated_list}')

# using append
appended_list = []
for i in range(5):
    appended_list.append(i)
print(f'list using append(): {appended_list}')

# using copy

original_list = [1, 2, 3]
copied_list = original_list.copy()
print(f'list using copy(): {copied_list}')