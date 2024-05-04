# Python program to take an integer as input and check it is prime or not...

num = int (input("Enater a number : "))

for i in range (2,num):
    if(num%i==0):
        print(f"{num} is not a prime number.")
        exit()
print(f"{num} is a prime number.")