# enter an 5 integer and sort it in ascending order

list = []
print("Enter five integers : ")
for i in range(5):
    x=int(input())
    list.append(x)
print(f"input list : {list}")
list.sort()
print(f"output list : {list}")
print("output list :",list[:-1])