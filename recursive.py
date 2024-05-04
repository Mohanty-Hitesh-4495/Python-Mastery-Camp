# recursive function to find the factorial of a number...

""" def fact(n):
    if not isinstance(n,int) or  n<0 :
        print("Not a valid input :(")
        return
    if n==0:
        return 1
    return n*fact(n-1)

print(fact('5.2'))
print(fact(54))
print(fact(-45))
print(fact(5.2))
 """

# function calling another function...
def greet(name):
    print(name)
    
def gm(gr,name):
    print("Hi!")
    greet(name)
    print("Good Morning")

gm(greet,"hitesh")
