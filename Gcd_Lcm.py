import math

# Function to calculate the greatest common divisor (GCD) of two numbers
def getgcd(num1, num2):
    return math.gcd(num1, num2)

# Function to calculate the least common multiple (LCM) of two numbers
def getlcm(num1, num2):
    return num1 * num2 // getgcd(num1, num2)

# Function to calculate the GCD of three numbers
def GCD(num1, num2, num3):
    a = getgcd(num1, num2)
    return getgcd(a, num3)

# Function to calculate the LCM of three numbers
def LCM(num1, num2, num3):
    a = getlcm(num1, num2)
    return getlcm(a, num3)

# Taking input from user
num1 = int(input("Enter first Integer:"))
num2 = int(input("Enter Second Integer:"))
num3 = int(input("Enter third number:"))

# Printing GCD and LCM
print("GCD = ", GCD(num1, num2, num3))
print("LCM = ", LCM(num1, num2, num3))
