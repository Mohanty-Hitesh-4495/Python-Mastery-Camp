# OOPs In Python 
# There are three different kind of animals 
# Dog, Cat, Mouse... 
# Cat is having attribute name, and (private) age
# Dog is having name (private), age and colour
# Mouse is having attribute colour and size(length)
# Create two object from each class and check whether the dog objects are having same name has the cat object
# and dog object having colour is matching with mouse object

class Dog:
    def __init__(self,name,age,col):
        self.__name__=name
        self.age=age
        self.colour=col

    def get_name(self):
        return self.__name__

class Cat:
    def  __init__(self,name,age):
        self.name=name
        self.__age__=age
    
    def get_age(self):
        return self.__age__

class Mouse:
    def __init__(self,col,size):
        self.colour=col
        self.size=size

d1=Dog("Tommy",3,"Brown")
c1=Cat("Tommy",5)
m1=Mouse("Brown",25)

if d1.get_name()==c1.name:
    print("Dog name is same as Cat")
else:
    print("Dog is not having same name as Cat")

if d1.colour==m1.colour:
    print("Dog is having same name as Mouse")
else:
    print("Dog is not having same name as Mouse")