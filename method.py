""" def meh(c,x=5):
    print(x)
    print(c)

meh(60,45)
meh(x=512,c=89) """

# write a method that takes two methods as arguements.
""" def meh(a,b):
    a()
    b()

def greet():
    print("Hi !",end=" ")

def name():
    print("Hitesh")

meh(greet,name) """

# define a recursive function
""" def fun(n):
    if n<0:
        return 
    if n<=1:
        return 1
    return n*fun(n-1)
print(fun(0)) """

# define any method or function that calls another function inside it

""" def fun(wish,name):
    greet(wish,name)

def greet(w,n):
    print(w,n)

fun("hi","hitesh") """

# define a method that takes one string as input and returns the first and last vowel present in the string

""" def vowel(word):
    l=['a','e','i','o','u']
    for i in reversed(word):
        if i in l:
            return i       
print(vowel("hitesh"))
print(vowel('Adyasha')) """

# def a function 'hi' if no arguements is passed and returns 'hello' if any arguements is passed

""" def meh(*val):
    if len(val) == 0:
        return "Hi"
    else:
        return "Hello"
"""

""" print(meh("Hi"))
print(meh("hitesh"))
print() """

# def a function 'hi' if no arguements is passed and returns 'hello' if any arguements is passed
# this logic wont work for all cases

""" def xyz(x,s='Hi'):
    if s != 'hi':
        return "hello"
    else:
        return "hi" """

# 

""" x=4

def fun1(x):
    x=5
    return x**2

def fun2():
    return x+7

def fun3(a):
    global x
    x=a
    return x+2
print(x)
print(fun1(3))
print(fun2())
print(fun3(8))
# x=9
print(fun2()) """

#  write a program that defines two globgal variables 'a' and 'b'. where 'a' is a number 'b' is a string
# furthur define a method that takes these two global variables as default arguements and returns true if the number of digits is greater than number of characters in the string.
""" 
a=(int)(input("Enter an integer :"))
b=input("Enter an string :")

def meh(x=a,y=b):
    if len(str(x)) > len(y):
        return True
    else:
        return False

print(meh(a,b))    
a=48646
print(meh(a,b))
print(meh())
 """

# define a method named as 'powerof' with two arguements 'x' and 'y' such that it returns x^y
# if provision for the default value y=2

""" x=int(input("Enter the x: "))
y=int(input("Enter the y: "))
def powerof(x,y=2):
    return x**y

print(powerof(x,y))
print(powerof(x)) """

# define a funtion that takes positional arguements and print there types sorted lexicographical

""" def typesort(*val):
    l=[str(type(i)) for i in val]
    l.sort(reverse=True)
    return l

print(typesort(45,"cbsh0",84.1564,456+6j,True)) """

# define a method that takes variable number of keyword arguements 
# prints all the arguements such that the strings will appear first followed by the rest as they have appeared in the function call

""" def huii(**val):
    l=[y for x,y in val.items() if type(y)==str]
    for x,y in val.items():
        if type(y)!=str:
            l.append(y)
    return l

print(huii(n=4654,n1=164,n2=4654,n3="scvdbu",n4="schbsdv",n5=548,n6=464,n7="scb")) """

# define a method or function of your choice that can take maximum three positional arguements
""" def huii(val1=45,val2=49,val3=79):
    print(val1)
    print(val2)
    print(val3)
    return 


huii(64,55,456)
huii(454,46)
huii("csbhj",4654,646,46546,161) """


# define a function that convert farheinet to celcius if no parameter is given the return 0
def temp(fr=0):
    if fr==0:
        return fr
    return (fr-32)*(5/9)
print("Temp = ",temp(49),"c")
print(temp())