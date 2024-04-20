import json

json_string = '''
{
    "student": [
            {
                "id": 1,
                "name": "Mohamed",
                "age": 23
            },
            {
                "id": 2,
                "name": "Omar",
                "age": 20
            }
        
    ]
}
'''
# decode JSON data into Python objects.

'''
- json.loads(): This function is used to decode JSON data from a string. 
  It takes a JSON-formatted string as input and returns a Python object.

- json.load(): This function is used to decode JSON data from a file-like object.
  It takes a file-like object (such as a file opened in read mode) as input and returns a 
  Python object.
'''

students = json.loads(json_string)
print(students['student'][0])

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# encode Python objects into JSON format. 
json_data = json.dumps(data)
print(json_data)
print(type(json_data))

# Writing to a JSON File
with open('data.json', 'w') as json_file:
    json.dump(data, json_file)
    print(type(json_file))

# Reading from a JSON File
with open('data.json', encoding='utf-8') as f:
    data = json.load(f)
    print("data os data file:", data)
    print(type(data))


