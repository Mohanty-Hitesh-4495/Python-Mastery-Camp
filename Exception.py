# Introduction To Exception Handling in python
""" try:
    x=int(input("Enter an integer :"))
    y=5/x
except Exception as e:
    print("Error",e)
else:
    print(x)
finally:
    print("Thnak you !!!") """



# Day-2 Practice (Handling Multiple Exceptions) 
""" class unknown:
    pass
    
x=5
z= unknown()

try:
    y=int(input("Enter an integer:"))
    print(z.age)
    z.age=x/y
except (AttributeError,ZeroDivisionError) as e:
    print(f"Exception={e}")
except Exception as e:
    print(f"Exception={e}")
else:
    print(z.age)
finally:
    print("Thanks") """



# Day-2 Practice (Age Exception Handling)
""" try:
    age=int(input("Enter your age:"))
    if age<0:
        raise Exception("Negative Number")
except Exception as e:
    print(f"Exception={e}")
else:
    print(age)
finally:
    print("Thank You") """

# Factorial of given number and handle the exception 
# factorial method returns factorial of given number
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

try:
    num=int(input("Enter your number:"))
    if num<=0:
        raise Exception("Negative Number")
except Exception as e:
    print(f"Exception={e}")
else:
    print(factorial(num))
finally:
    print("Thank You") 
    

#  