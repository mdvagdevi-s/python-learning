def outer(name):
    def inner():
        print("Hello",name)
    return inner

x=outer("VAgdevi")
y=outer("Shilpa")
x()
y()