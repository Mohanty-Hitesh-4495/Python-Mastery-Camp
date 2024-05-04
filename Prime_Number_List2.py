# Given a List of prime numbers... 
# Make a list of Two digit prime numbers from that list...

list = [2,3,53,37,89,93]
list2 = [i for i in list if i>10 and i<100]
print("Current Prime Number List:")
print(list)
print("Two Digits Prime Numbers:")
print(list2) 