import numpy as np

# Create a 3x3 matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Add a vector to each row of the matrix using broadcasting
vector = np.array([10, 20, 30])
result = matrix + vector

print("Original Matrix:")
print(matrix)
print("\nVector:")
print(vector)
print("\nResult after Broadcasting:")
print(result)
