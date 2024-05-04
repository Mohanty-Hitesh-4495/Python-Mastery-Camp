#  design a timer

from datetime import datetime, timedelta
import time

""" 
current_date = datetime.now()
print(current_date)
any_date = input("Enter a date in dd/mm/yyyy format : ")
any_date = datetime.strptime(any_date,"%d/%m/%Y")  # %
print(f"{any_date.day}/{any_date.month}/{any_date.year}")
# print(any_date,%d-%m-%Y)
print(any_date)

"""
# 
""" d = datetime(2024,3,10,10,55,5)
print(d)
"""

# timer in seconds
""" 
for i in range(10,-1,-1):
    # da = datetime.now()
    # print(da)
    print(f"{i} seconds left")
    time.sleep(1)
"""

# alarm set for upcomin event using timedelta
""" d = datetime.now()
e = d+timedelta(days= 30)
while d < e:
    d = datetime.now()
print("Ring the bell") """


# date after specified days or time
""" d = datetime.now()
e = d+timedelta(days= 30)
print(d)
print(e) """


# calculate the time taken by programe to execute
""" d = datetime.now()
for i in range(10000):
    print(i)
print("Suiiiii :)")
e = datetime.now()
print(e-d) """

# wrrite an program to find out the remaining days for upcoming bday from user DOB
""" dob = input("Enter your DOB in yyyy-mm-dd format : ")
DOB = datetime.strptime(dob,'%Y-%m-%d')
CD = datetime.now()
NBD = datetime(CD.year+1,DOB.month,DOB.day) - CD
print(NBD)
 """

# defining an 2D-array
# learning numpy package 
# import numpy as np
""" a=[[1,2],[3,4]]
A=np.array(a)
B=np.transpose(A)
C=np.reshape(A,[4,1])
D=np.matmul(A,B)
E=np.add(A,B)
F=np.dot(A,B)
print("Array :\n",A)
print("Transpose :\n",B)
print("Reshap :\n",C)
print("Matrix Multiplication :\n",D)
print("Addition :\n",E)
print("Dot :\n",F) """


# Matrix manupilation using numpy library 
""" import numpy as np
a=np.array([[1,2,3],[4,9,6],[1,8,9]])
b=np.linalg.inv(a)
c=np.matmul(a,b)
d=np.linalg.det(a)
print("Array :\n",a)
print("Inverse :\n",b)
print("product of Array 'a' and its inverse 'b' :\n",c)
print("Determinent :\n",d) """

# Average of an matrix using numpy library
""" import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.average(a)
print("Array :\n",a)
print("Average of matrix A :\n",b) """

# 
""" import numpy as np
a=np.array([[1,2,3],[4,9,6],[1,8,9]])
x=np.eye(3)
dia=np.diag(a)
print("Identity Matrix :\n",x)
print("Matrix :\n",a)
print("Diagonal values :\n",dia) """



# Given a matrix, generate another matrix such that every element will be the sum of its neighbours

def generate_neighbor_sum_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    neighbor_sum_matrix = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            # Iterate over each neighbor of the current element (i, j)
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    # Check if the neighbor indices are within bounds
                    if 0 <= x < rows and 0 <= y < cols:
                        # Exclude the current element itself
                        if (x, y) != (i, j):
                            neighbor_sum_matrix[i][j] += matrix[x][y]

    return neighbor_sum_matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
print_matrix(matrix)

neighbor_sum_matrix = generate_neighbor_sum_matrix(matrix)

print("\nNeighbor Sum Matrix:")
print_matrix(neighbor_sum_matrix)
