# create class student that takes 3 marks and has method average().

class Student:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def average(self):
        avg=(self.m1+self.m2+self.m3)/3
        return avg
s1=Student(10,20,30)

print("AVERAGE:",s1.average())
