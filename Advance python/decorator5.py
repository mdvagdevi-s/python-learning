def log_call(func):
    def wrapper(*args,**kwargs):
        print("Function is being called")
        func(*args,**kwargs)
        print("Function finished")
    return wrapper

@log_call
def greet(*name):
    for n in name:
        print("Hello",n)

greet("Vagdevi","Sohan")
