# Write a python program to find the 4-point DFT of any sequence. 
# take input the sequence {1,2,1,2}.
# 4-point DFT of a sequence is just a matrix multiplication w*s.

# w=[ 1    1   1   1
#     1   -j  -1   1
#     1   -1   1  -1
#     1    1  -1  -j]
 
# i=[1
#    2
#    1
#    2]

import numpy as np

l = []
print("Enter an list having 4 values:")
for i in range(4):
    num = int(input(f"Value {i+1}:"))
    l.append(num)

l = np.matrix(l)
l = np.transpose(l)
print("Given Four Points :")
print(l)
w = np.matrix([[1, 1, 1, 1],
              [1, -1j, -1, 1j],
              [1, -1, 1, -1],
              [1, 1j, -1, -1j]])
print("W Matrix:")
print(w)
dft_result = np.transpose(np.matmul(w, l))
print("4-point DFT of the sequence:\n", dft_result)