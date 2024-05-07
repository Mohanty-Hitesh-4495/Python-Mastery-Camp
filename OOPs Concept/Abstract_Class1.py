from abc import ABC

class animal(ABC):
    def sound(self):
        pass

class dog(animal):
    def sound(self):
        print("BHUA BHAU....")

class cat(animal):
    def sound(self):
        print("MEAW MEAW....")

c=cat()
d=dog()
c.sound()
d.sound()