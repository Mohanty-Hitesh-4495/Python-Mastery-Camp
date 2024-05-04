# write a python programe to find the range of integer values present in a given matrix
import numpy as np

row = int(input("Enter the number of row : "))
clm = int(input("Enter the number of column : "))
mat = []

for i in range(row):
    n=list(map(int,input().split()))
    mat.append(n)

matrix = np.array(mat)
min = np.min(matrix)
max = np.max(matrix)
print("start = ",min)
print("end = ",max)