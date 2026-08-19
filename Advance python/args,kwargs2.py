def profile(*args, **kwargs):
    print("Subject:")
    for i in args:
        print(i)
    print("Details:")

    for key,value in kwargs.items():
   
        print(key,":",value)

profile("Python", "DSA", name="Vagdevi", age=20)