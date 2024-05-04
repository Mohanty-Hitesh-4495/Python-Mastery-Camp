# Define a function 'sumint' to calculate the sum of integers using variable number of arguments
# 'x' is used with asterisk (*) to denote variable number of arguments, stored in a tuple

def sumint(*x): 
    sum=0 
    for i in x:
        sum+=i
    return sum

def numargs(*many):
    return len(many)

print(sumint(1,5,6,3,2,4,4,4566,465,465,565,465,456,45))
print(numargs(456,5,5,3,5,5,62,351,56,564,65))