# class student and Dog having same attributes ()

class Dog:
    def __init__(self,name,age,col):
        self.name=name
        self.age=age
        self.colour=col

class student:
    age=20
    def __init__(self,name):
        self.name=name
    
    def info(self):
        print("Nameb =",self.name," Age =",self.age)
    
    @staticmethod
    def fun(s,r):
        print("Suiiiii")
        # s.info()
        print(f"{s.name} is older than {r.name}") if s.age>r.age else print(f"{r.name} is older than {s.name}")

obj = student("Sudhansu")  # objectb of student class 
obj1 = student("Manohar")
obj.info()
obj1.info()
obj1.age=19  # manohar: age=19
obj.info()    
obj1.info()

obj.roll=12  # new attribute is created roll for sudhanshu

student.age=18  # student class default age=18
obj.info()      
obj1.info()  # object assigned with age wont be affected

obj2 = student("Smarak")  # new object for Student class 
obj2.info() 

# obj.fun(obj1)  # shows error ! 
student.fun(obj,obj1)  # passinfg object as arguement

D1=Dog("Tommy",6,"Brown")  # object of Dog class
D2=Dog("Jack",5,"White")

student.fun(D1,D2)  # we can pass Dog class object to Student class function as an arguement 
# since fun() function is static


