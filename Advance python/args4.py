def student(name, *subjects):
    print("Name:",name)
    print("Subjects:")

    for i in subjects:
        print(i)

student("Vagdevi","Python","Dsa","Sql")