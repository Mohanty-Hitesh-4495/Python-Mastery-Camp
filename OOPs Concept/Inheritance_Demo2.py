class Parents:
    fam="Wellcome to the Mohanty Family 👨‍👩‍👦‍👦"
    
class Father(Parents):
    fname="Rabindranath"

class Mother(Parents):
    mname="Bhagylata"

class Student(Father,Mother):
    _name="" 
    age=0
    def __init__ (self,name,age): #constructor
        self.name=name
        self.age=age
    
    def getage(self): #method returns age
        return self.age

class house(Student):
    housename=""
    def __init__ (self,name,age,hname):
        super().__init__(name,age)
        self.housename=hname
    
    def gethousename(self):
        return self.housename

class Section(house):
    secname=""
    def __init__(self,name,age,hname,secname):
        super().__init__(name,age,hname)
        self.secname=secname
    
    def getsecname(self):
        return self.secname

s=Student("Hitesh",21)
h=house("Syed",20,"Visves")
sec=Section("Rahul",23,"MCA","Genius")
print("***Student***")
print(s.fam)
print(s.name)
print(s.age)
print(s.fname)
print(s.mname)
print(s.getage())
print("***House***")
print(h.name)
print(h.age)
print(h.gethousename())
print("***Section***")
print(sec.name)
print(sec.age)
print(sec.gethousename())
print(sec.getsecname())
