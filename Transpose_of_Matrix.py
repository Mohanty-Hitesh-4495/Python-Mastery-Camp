# Function to calculate the transpose of a matrix
def transpose(m):
    transpose=[]
    for i in range(len(m[0])):
        row=[]
        for j in range(len(m)):
            row.append(m[j][i])
        transpose.append(row)
    return transpose


matrix=[]
r=int(input("Enter the number of row:"))
c=int(input("Enter the number of column:"))
for i in range(r):
    row=[]
    for j in range(c):
        row.append(int(input(f"Enter a number to [{i}][{j}] index :")))
    matrix.append(row)

transpose = transpose(list)

# Print the original matrix
print("Current matrix:")
for i in list:
    print(i)

# Print the transpose matrix
print("Transpose Matrix:")
for i in transpose:
    print(i)
