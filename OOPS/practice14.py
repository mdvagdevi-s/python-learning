from abc import ABC, abstractmethod

class Vehicle:
    @abstractmethod
    def start(self):
        pass
    def stop():
        pass

class car:
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

c=car()
c.start()
c.stop()