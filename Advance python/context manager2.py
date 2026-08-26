class Test:

    def __enter__(self):
        print("Start")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Error:", exc_value)
        return True


with Test():
    print(10 / 0)

print("Program continues")