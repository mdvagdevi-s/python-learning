# create class student that takes 3 marks and has method average().

class Student:
    def __init__(self,name,list_of_marks):
        self.name=name
        self.list_of_marks=list_of_marks
    def average(self):
        sum=0
        for eachvalue in self.list_of_marks:
            sum=sum+eachvalue
        average=sum/3
        print("Average is:",average)
student1=Student("Adi",[90,98,99])
student1.average()
