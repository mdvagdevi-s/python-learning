import json

data = '{"name": "Vagdevi", "age": 20, "branch": "CSE"}'

student = json.loads(data)

print(student)
print(type(student))