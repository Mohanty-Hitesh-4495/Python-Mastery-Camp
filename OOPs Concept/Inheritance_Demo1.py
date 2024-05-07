# Simple demo program illustrating the use of the super() function in Python:

class Father:
    fname = ""

    def __init__(self, fname):
        self.fname = fname

    def display1(self):
        print(f"Father's name = {self.fname}")


class Mother:
    mname = ""

    def __init__(self, mname):
        self.mname = mname

    def display2(self):
        print(f"Mother's name = {self.mname}")


class Son(Father, Mother):
    name = ""

    def __init__(self, name, fname, mname):
        self.name = name
        super().__init__( fname)  # Call Father's constructor explicitly
        super(Father,self).__init__( mname)  # Call Mother's constructor explicitly

s = Son("Hitesh", "Rabindranath", "Bhagyalata")
print(s.name)
s.display1()
s.display2()
