def double_result(func):
    def wrapper(*args,**kwargs):
        print("Function is being called")
        result=func(*args,**kwargs)
        print("Function finished!")

        return result*2
    return wrapper

@double_result
def add (a,b):
    return a+b

result = add(10, 20)
print("Result:", result)