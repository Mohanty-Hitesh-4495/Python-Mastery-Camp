file=open("friends.txt","w")
n = int(input("Enter the numbre of Students:"))
bl=[]
gl=[]

for i in range(n):
    name=input("Enter the Name:")
    gender=input("Enter Gender:")
    age=(input("Enter Age:"))
    if gender.lower() == "male" or gender.lower() == "m":
        bl.append([name,gender,age])
    else:
        gl.append([name,gender,age])

gl.sort(key = lambda x: int(x[2]))
gl.sort(key = lambda x: int(x[2]))

for i in range(len(gl)):
    file.write(",".join(i)+"\n")
for i in range(len(bl)):
    file.write(",".join(i)+"\n")
