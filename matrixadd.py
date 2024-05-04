list1=[]
list2=[]
addlist=[]

r=int(input("Enter the number of row:"))
c=int(input("Enter the number of column:"))

print("Enter elements to the first array:")
for i in range(r):
    row=[]
    for j in range(c):
        row.append(int(input(f"Enter a number to [{i}][{j}]index :")))
    list1.append(row)
    
print("Enter elements to the Second array:")
for i in range(r):
    row=[]
    for j in range(c):
        row.append(int(input(f"Enter a number to [{i}][{j}]index :")))
    list2.append(row)

# adding two arrays
for i in range(r):
    row=[]
    for j in range(c):
        row.append(list1[i][j]+list2[i][j])
    addlist.append(row)

print("Addition of two arrays:")
for i in addlist:
    print(i)