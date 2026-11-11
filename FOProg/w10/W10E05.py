# Week 10 - Example 5
# Import the json module
import json

# Create a dictionary representing a person
person = {
    'name': 'Alice',
    'age': 25,
    'hobbies': ['reading', 'writing', 'coding']
}

# Convert the dictionary to a JSON string using json.dumps()
person_json = json.dumps(person)
print("JSON formatted string:", person_json)
# Expected output:
# {"name": "Alice", "age": 25, "hobbies": ["reading", "writing", "coding"]}

# Convert the JSON string back to a dictionary using json.loads()
person_dict = json.loads(person_json)
print("Converted back to dictionary:", person_dict)
# Expected output:
# {'name': 'Alice', 'age': 25, 'hobbies': ['reading', 'writing', 'coding']}
