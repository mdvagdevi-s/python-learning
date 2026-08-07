from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop():
        pass

class car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

c=car()
c.start()
c.stop()