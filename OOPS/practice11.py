class person:
    def __init__(self,name):
        self.name=name

    def display(self):
        print(self.name)

class Student(person):
    def __init__(self, name,roll):
        super().__init__(name)
        self.roll=roll
    def details(self):
        print("Roll:",self.roll)

s=Student("Vagdevi","4KV24CS159")
s.display()
s.details()
    