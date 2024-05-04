# define a function to check whether a given list has only integer 
# list should have only integers

def intlist(l):
    if not isinstance(l,list):
        return "Invalid Arguement Passed"
    for i in l:
        if not isinstance(i,int) or isinstance(i,bool):
            return False
    return True
        
l=[1,5,4,56,'ca',"csvs",True,]
l1=[1,5,78,6,65,5,6]
l2=[1,5,False,78,6,65,5,6]
l3=["sbvjh0","sddnkjs",57616,5,9,54,9,45]

print(intlist(l))
print(intlist(l1))
print(intlist(l2))
print(intlist(l3))
print(intlist(set(l)))