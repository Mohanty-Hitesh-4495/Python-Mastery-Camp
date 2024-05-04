# Generate a matrix of size (m x n)
# Where each row is having all the value same as the row number 

import numpy as np
m=int(input("enter the row number:"))
n=int(input("enter the column number:"))
l = [[i+1 for j in range(m)]for i in range(n)]
l = np.matrix(l)
print(l)