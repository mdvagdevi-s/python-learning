import json

student = {
    "name": "Vagdevi",
    "marks": 95
}

with open("Advance python/student2.json", "w") as file:
    json.dump(student, file)