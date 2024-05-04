# IDFT {8 0 0 0}
""" import numpy as np

l = []
print("Enter an list having 4 values:")
for i in range(4):
    num = int(input(f"Value {i+1}:"))
    l.append(num)

l = np.matrix(l)
l = np.transpose(l)
print(l)
w = np.matrix([[1, 1, 1, 1],
              [1, 1j, -1, -1j],
              [1, -1, 1, -1],
              [1, -1j, -1, 1j]])
print(w)
dft_result = 0.25 * np.transpose(np.matmul(w, l))
print("4-point DFT of the sequence:\n", dft_result) """





    