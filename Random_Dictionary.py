# make a list of n prime numbers 
# make another list of n random numbers
# make sure that in both list there will be no duplicates 
# make a dictionary such that each element from the first list is the key and the element of second list is value.

import random

def isprime(num):                       # Checks for number is prime or not
    for i in range(2,num//2):
        if num%i==0:
            return False
    return True

pl=[]                                   # Prime number List
rl=[]                                   # Random numbers List
n=int(input("Enter the size of list :"))

while len(pl)!=n: 
    num=int(random.randint(1,100))      # Generating prime numbers randomly
    if isprime(num):
        pl.append(num)

for i in range(n):                      # Generating random numbers  
    num=int(random.randint(1,100))
    if num not in rl:
        rl.append(num)

print("Random list :",rl)
print("Prime list :",pl)

disc=dict()                             # makes an dictionary 
for i in range(len(pl)):                # having prime number as key
    disc[pl[i]]=rl[i]                   # and random number as value
    
print(disc)
    




