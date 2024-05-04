# Python Program to find out the factorial of a given number.


# Function to calculate factorial using iterative approach
def fact1(num):
    for i in range(2,num):
        result=result*i
    return result


# Function to calculate factorial using recursive approach
def fact2(num):
    if (num<0):
        return 0
    if (num==0):
        return 1
    return fact2(num-1)*num

# Take user input for the number
number = int(input("Enter the number :"))
result1 = fact2(number)
result2 = fact2(number)
print(f"Factorial of {number} is {result1}")
print(f"Factorial of {number} is {result2}")
