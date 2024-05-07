# Student class 
class Student:
    # no need of defining the instances variable in class. if they are asssigned in constructor
    # their is flexibility in python
    def __init__(self,name="name",roll=0):
        self.name=name
        self.roll=roll
    
    # defining a method to display data members of Student class
    def display(self):
        print(self.name,self.roll)

# s is the object of Student class...
s=Student("Hitesh",36)
# s.roll="007"        # type of variables of student class can be modifyed even if its type is definrd in that class
# s.name="Bond"
print(s.name,s.roll)  # roll is converted into String type

# creating another object r of Student class 
r=Student("Syed",67)  
# r.roll=8
print(r.name,r.roll)
# print(type(r.roll))

# 
z=Student()
print(z.name,z.roll)

x=Student(roll=37)
# del x.roll            # del keyword is used to delete a memeber of a class for an object
print(x.name,x.roll)

y=Student(name="Prakash")
print(y.name,y.roll)

hitu = s
del s                   # 
# print(hitu)
print(hitu.name,hitu.roll)


