def student(name,age,*subjects,branch):
    print("Name:",name)
    print("Age:",age)
    print("Subjects:",subjects)
    print("Branch:",branch)

data={"name":"Vagdevi","age":20,"branch":"CSE"}
subjects=["Python","DSA","SQL"]

student(data["name"],data["age"],*subjects,branch=data["branch"])


#The *subjects means:
#Everything after name and age that is positional goes into subjects.
#And branch comes after *subjects, so branch must be provided as a keyword argument.