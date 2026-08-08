class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grade:", self.grade)

s = Student("Vagdevi", 20, "A")
s.display()