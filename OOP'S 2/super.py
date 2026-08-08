class parent():
    def greet(self):
        print("Hello")

class child(parent):
    def greet(self):
        super().greet()
        print("Welcome student")

s=child()
s.greet()