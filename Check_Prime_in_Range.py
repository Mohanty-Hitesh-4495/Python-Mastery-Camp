# Python program to take a (Start-End) range...
# Print all Prime numbers within that range...

def prime(num):
    for i in range (2,num):
        if num%i==0:
            return False
    return True
    
start = int (input("Enter the starting range :"))
end = int (input("Enter the ending range :"))
print(f"Prime Nummbers in Range ({start}-{end})")
for i in range(start,end+1):
    if prime(i):
        print(i,end=" ")