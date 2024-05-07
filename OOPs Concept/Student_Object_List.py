#  create a list of students and sort them as per thier roll no., age, cgpa and name

class Student:

    def __init__(self,n,r,a,c):
        self.name=n
        self.roll=r
        self.age=a
        self.cgpa=c
    def display(self):
        print("Name :",self.name," Roll:",self.roll," Age:",self.age," Cgpa:",self.cgpa)

no=int(input("Enter the number of Students:"))
l=[]

for i in range(no):
    print(f"Enter the details of Student {i}")
    n=(input("Enter the Name :"))
    r=int(input("Enter the Roll :"))
    a=int(input("Enter the Age :"))
    c=float(input("Enter the Cgpa :"))
    obj=Student(n,r,a,c)
    l.append(obj)

opt=0
while(True):
    print("***** Main Menu *****")
    print("1. Name-wise Sorting")
    print("2. Roll-wise Sorting")
    print("3. Age-wise Sorting")
    print("4. Cgpa-wise soerting")
    print("5. Exit")
    opt=int(input("Enter your Choice:"))

    if opt==1:
        sl=sorted(l,key=lambda x : x.name)
    elif opt==2:
        sl=sorted(l,key=lambda x : x.roll)
    elif opt==3:
        sl=sorted(l,key=lambda x : x.age)
    elif opt==4:
        sl=sorted(l,key=lambda x : x.cgpa)
    elif opt==5:
        print("Exiting From Menu")
        break
    else :
       print("Invalid Choice !!!")

    for i in range(no):
            sl[i].display()



     
 
