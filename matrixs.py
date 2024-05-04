# take a matrix as input and print it
r=int(input("enter the number of rows:"))
c=int(input("enter the number of colums:"))
list=[]
print("Enter integers to the matrix:")
for i in range(r):
    row=[]
    for j in range(c):
        row.append(int(input(f"add a value to [{i}][{j}] index :")))
    list.append(row)

for i in list:
    print(i)