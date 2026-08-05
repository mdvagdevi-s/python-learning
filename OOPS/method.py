class Student:
    def __init__(self,name):
        self.name=name
    def hello(self):
        print("Hello",self.name)
s1=Student("Vagdevi")
s1.hello()