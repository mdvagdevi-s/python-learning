from dataclasses import dataclass
@dataclass
class Student:
    name:str
    age:int
    marks:int=89

s=Student("Vagdevi",21)
print(s)
