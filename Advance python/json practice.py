import json

student = {
    "name": "Vagdevi",
    "age": 20,
    "branch": "CSE"
}

data = json.dumps(student)

print(data)
print(type(data))