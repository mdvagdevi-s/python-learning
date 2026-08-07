from abc import ABC ,abstractmethod

class animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class dog(animal):
    def sound(self):
        print("Dog Barks bowbowbow")
s=dog()
s.sound()