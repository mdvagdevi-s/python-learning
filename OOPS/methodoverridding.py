class Animal:
    def sound(self):
        print("Animal makes sounds")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

d=Dog()
d.sound()