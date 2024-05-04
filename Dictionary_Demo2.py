#  make a dictionary of body parts and function
n=int(input("Enter the number of body parts:"))
parts={}

for i in range(n):
    key=(input("Enter a body part name:"))
    parts[key]=(input("Enter the function :"))
    
print(parts)

# Search for body parts with the given function
search=(input("Enter the function to search the part:"))
for i in parts.keys():
    if parts[i]==search:
        print(i)

# Using list comprehension to find body parts with the given function
print([x for x in parts if parts[x]==search])