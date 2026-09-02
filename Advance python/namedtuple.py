from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "branch"])

s = Student("Priya", 20, "CSE")

print(s.name)
print(s.age)
print(s.branch)