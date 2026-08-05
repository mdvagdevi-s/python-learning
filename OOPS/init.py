class Student:
    school_name="ABC"
    def __init__(self,name):
        #print("Whenever a new object is created I am called automatically")
        #print(self)
        self.name=name

s1=Student("Vagdevi") #init method called

print("Student 1",s1.name)
print(s1.school_name)
s2=Student("Sohan")
print("Student 2",s2.name)