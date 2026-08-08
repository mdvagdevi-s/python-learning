from abc import ABC , abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        print("Radius of circle is:",3.14*self.radius*self.radius)


c=circle(5)
c.area()