
from abc import ABC ,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class square(shape):
    def area(self,side):
        return side*side

class rectangle(shape):
    def area(self,l,b,h):
        return l*b*h

s=square()
print(s.area(5))
r=rectangle()
print(r.area(2,3,4))