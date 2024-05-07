#  define a rectangle class and print in ascending order

class Rectangle:
    def __init__(self,l,w):
        self.length=l
        self.width=w
    def display(self):
        print("Length :",self.length," Width:",self.width," Area:",self.getarea())
    def getarea(self):
        return self.length*self.width
    def getperimeter(self):
        return 2*(self.length+self.width)
    
def areasort(l):
    sl=sorted(l,key=lambda x : x.getarea())
    return sl

def lensort(l):
    sl=sorted(l,key=lambda x : x.length)
    return sl

def widsort(l):
    sl=sorted(l,key=lambda x : x.width)
    return sl

def perisort(l):
    sl=sorted(l,key=lambda x : x.getperimeter())
    return sl 

n=int(input("Enter the number of Rectangle:"))
l=[]

for i in range(n):
    print(f"Enter the details of Rectangle {i}")
    len=float(input("Enter the length :"))
    wid=float(input("Enter the width :"))
    obj=Rectangle(len,wid)
    l.append(obj)

opt=0
while(True):
    print("***** Main Menu *****")
    print("1. Area-wise Sorting")
    print("2. Length-wise Sorting")
    print("3. Width-wise Sorting")
    print("4. Perimeter-wise soerting")
    print("5. Exit")
    opt=int(input("Enter your Choice:"))
    if opt==1:
        l=(areasort(l))
    elif opt==2:
        l=(lensort(l))
    elif opt==3:
        l=(widsort(l))
    elif opt==4:
        l=(perisort(l))
    elif opt==5:
        print("Exiting From Menu")
        break
    else:
        print("Invalid choice !!!")
    for i in range(n):
        l[i].display()