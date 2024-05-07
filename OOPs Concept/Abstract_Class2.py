# Define an abstratct class "shape" with an abstract method "area"

from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class cicle(shape):
    def __init__(self,r):
        self.radius=r
    def area(self):
        return 3.141*self.radius

class rectangle(shape):
    def __init__(self,l,w):
        self.length=l
        self.width=w

    def area(self):
        return self.length*self.width

obj = cicle(12)
print(obj.area())
obj = rectangle(12,6)
print(obj.area())

