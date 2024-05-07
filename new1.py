class Rectangle:
    
    def __init__(self,length=0,width=0):
        self.length=length
        self.width=width
    
    def display(self):
        print(f"Length = {self.length}")
        print(f"Width = {self.width}")

    def area(self):
        return self.length*self.width
    
    def peri(self):
        return 2*(self.length+self.width)
    
r=Rectangle(2.5,3)
r.display()
p=Rectangle(3,4.0)
r.display()

if r.area()>p.area():
    print("Area of r is  larger than p")
else:
    print("Area of r is not larger than p")
