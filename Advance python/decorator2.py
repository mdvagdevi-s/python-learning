def greet():
    print("Hello")
def execute(func):
    print("Starting")
    func()
    print("Finished!")

execute(greet)