def log_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")

        result = func(*args, **kwargs)

        print("Function finished")

        return result

    return wrapper

@log_call
def add(a, b):
    return a + b


result = add(10, 20)
print("Result:", result)