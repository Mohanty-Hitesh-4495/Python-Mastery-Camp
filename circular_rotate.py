def rowshift(matrix,k=1,row=True):
    if row==True:
        return [x[-k:]+x[0:-k] for x in matrix]
    else:
        return matrix[-k:]+matrix[0:-k]


matrix=[[4,5,9,1],[8,12,15,24],[3,4,2,1],[17,19,34,36]]
print(matrix)


# print(rowshift(matrix,2,False))
# print(rowshift(matrix,2))
print(rowshift(matrix))
print(rowshift(matrix,row=False))


""" x=[1,2,3,4]
print(type(x[-1]))
print((x[-1:])) """
