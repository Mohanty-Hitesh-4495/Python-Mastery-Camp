import Matrix as mat
import random as rnd


r=int(input("enter the number of rows:"))
c=int(input("enter the number of colums:"))
mat1=[]
mat2=[]
print("Enter integers to the matrix:")
for i in range(r):
    row1=[]
    row2=[]
    for j in range(c):
        row1.append(rnd.randint(1,50))
        row2.append(rnd.randint(1,50))
    mat1.append(row1)
    mat2.append(row2)

print("Matrix 1:=",mat1)
print("Matrix 2:",mat2)
print(mat.add(mat1,mat2))