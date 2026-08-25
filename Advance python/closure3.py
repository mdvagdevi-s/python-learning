def outer():
    message="Hello Vagdevi"

    def inner():
        print(message)
    return inner

x=outer()
x()