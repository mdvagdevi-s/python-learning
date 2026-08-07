from abc import ABC ,abstractmethod
class Dog:
    @abstractmethod
    def sound(self):
        pass

class cat:
    def sound(self):
        print("Cat says meow")

c=cat()
c.sound()