class animal:
    def eat(self):
        print("Animal is eating")

class dog(animal):
    def bark(self):
        print("Dog barks bowbowbow")

d=dog()
d.eat()
d.bark()