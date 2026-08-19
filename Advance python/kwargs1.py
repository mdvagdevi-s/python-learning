def student_info(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)
student_info(name="Vagdevi", age=20, branch="CSE")