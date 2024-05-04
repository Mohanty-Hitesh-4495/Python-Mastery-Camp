# Write a menu based program 
# 1. find transpose of matrix
# 2. Conjugate of matrix
# 3. mirror image of matrix

import numpy as np
m=int(input("enter the row number:"))
n=int(input("enter the column number:"))

l = [[complex(input(f"index[{j}][{i}]:")) for j in range(m)]for i in range(n)]
l = np.matrix(l)

print(l)

while True:
    print("*** Main Menu ***")
    print("1. Transpose")
    print("2. Conjugate")
    print("3. Mirror")
    print("4. Exit")
    opt = int(input("Enter your Choice :"))
    if opt==1:
        op = np.transpose(l)
        print(op)
    elif opt==2:
        op = np.conjugate(l)
        print(op)
    elif opt==3:
        op = np.flip(l)
        print(op)
    elif opt==4:
        break