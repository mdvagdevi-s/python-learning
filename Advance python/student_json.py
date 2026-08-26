import json

with open("Advance python/student.json","r") as file:
    student=json.load(file)

print(student["name"])