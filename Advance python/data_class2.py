from dataclasses import dataclass,field
@dataclass
class Student:
    name:str
    subjects:list[str]=field(default_factory=list)
s1=Student("Vagdevi")
s2=Student("Sohan")

s1.subjects.append("Python")

print(s1.subjects)
print(s2.subjects)