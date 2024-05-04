# Make a set of human body parts by asking user to supply the next input

n=int(input("Enter the number of body parts:"))
parts=set()
for i in range(n):
    p=(input("Enter a body part name:"))
    parts.add(p)
print(parts)
