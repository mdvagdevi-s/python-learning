def decorator(func):
    def wrapper(*args,**kwargs):
        print("Before")
        func(*args,**kwargs)
        print("After")

    return wrapper

@decorator
def greet(name):
    print("Hello",name)

greet("Vagdevi")