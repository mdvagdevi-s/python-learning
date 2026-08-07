class animal:
    def eat(self):
        print("Animal is eating")

class dog(animal):
    def bark(self):
        print("Dog barks")

d=dog()
d.eat()
d.bark()