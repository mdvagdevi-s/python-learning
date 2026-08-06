from abc import ABC ,abstractmethod


class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class car(vehicle):
    def start(self):
        print("Car starts with a button")

c=car()
c.start()