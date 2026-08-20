def student(name, age, branch):
    print("Name:", name)
    print("Age:", age)
    print("Branch:", branch)

details = {
    "name": "Vagdevi",
    "age": 20,
    "branch": "CSE"
}


student(**details)