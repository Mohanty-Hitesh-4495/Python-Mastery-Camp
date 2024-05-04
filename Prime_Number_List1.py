# write an python program to make a list of 10 prime numbers starting from 100

def isprime(n):
    if n<0:
        return False
    for i in range (2,n):
        if n%i==0:
            return False
    return True

list=[]
n=101
while len(list)<10:
    if(isprime(n)):
        list.append(n)
    n+=1
print(list)