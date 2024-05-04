class test:
    def __init__(self,x="name"):
        self.name=x

obj1=test()
obj0=test("Jadu")
obj2=test("Hitu")

l=[obj0.name,obj1.name,obj2.name]
s={obj1.name,obj0.name,obj2.name}
print(l)
print(s)