def decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper
@decorator
def greet():
    print("Hello")


#instead of writting this we use @decorator
#greet=decorator(greet)
greet()