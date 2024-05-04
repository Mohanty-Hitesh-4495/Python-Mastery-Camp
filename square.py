list=[1,5,6,9,45,6,1,16]
sq=[]
sq2=[i**2 for i in list]
for i in list:
    sq.append(i*i)
print(list)
print(sq)
print(sq2)