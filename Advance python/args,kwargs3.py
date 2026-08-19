def student_profile(name, *subjects, **details):
    print("Name:",name)
    print("Subjects:")
    for i in subjects:
        print(i)
    print("Details:")

    for key,value in details.items():
        print(key,":",value)

student_profile(
    "Vagdevi",
    "Python",
    "DSA",
    "SQL",
    age=20,
    branch="CSE"
)