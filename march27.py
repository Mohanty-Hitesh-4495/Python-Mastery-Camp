""" def fun(**args):
    print(args)
    for i in args:
        print(i)

fun(name="Emma",age="25") """

""" def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d

    return inner_fun(a, 20)
    return a

result = outer_fun(5, 10)
print(result) """

""" def display(**kwargs):
    for i in kwargs:
        print(i)

display(emp="Kelly", salary=9000) """

# 56	Convert the following for loop into while loop.
""" for i in range(10):
    for j in range(i):
        print ('$',end="\n")
    print("") """


# Implement a function print_fibonacci that takes an integer n as input and prints the first n Fibonacci numbers.
""" def fib(n):
    l=[]
    (a,b) = (0,1)
    for i in range(n):
        l.append(a)
        a,b = b,a+b
    return l

print(fib(1))
print(fib(2))
print(fib(5)) """

# Create a function is_armstrong that takes an integer as input and returns True if it's an Armstrong number, else False.
      
""" def amstrong(num):
    n=len(str(num))
    temp=num
    sum = 0
    while temp!=0:
        sum = sum + int((temp%10)**n)
        temp/=10
    return sum==num

print(amstrong(123))
print(amstrong(45654))
print(amstrong(1000))
print(amstrong(153))
print(amstrong(1634)) """


# 17	Define a function remove_duplicates that takes a list as input and returns a new list with duplicates removed.	
""" def remove_duplcate(l):
    return list(set(l))

print(remove_duplcate([1,5,4,32,4,56,1,4,232,4,55,32,326,6,56,2])) """

# binary search

def binarySearch(list,key):
    if len(list)==0:
            return -1
    
    mid = len(list)//2
    if key==list[mid]:
        return mid
    elif key>list[mid]:
        return mid+1+binarySearch(list[mid+1:],key)
    else:
        return binarySearch(list[:mid],key)
    
l=[1,2,4,5,7,9,10,12,13,46,79,89,102,125,149,150]
print(binarySearch(l,12))

