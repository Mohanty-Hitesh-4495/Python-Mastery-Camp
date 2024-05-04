# define a method that returns ther average of all the float numbers present in a list


def avg(l):
    count=0
    sum=0
    for i in l:
        if isinstance(i,float):
            sum+=i
            count+=1
    if sum==0:
        return "No float Numbers Found"
    return sum/count

l=[1,5,4,64,5,49,3,"ascgg",45.3,98.2,"abu",True]
print(avg(l))