# define a method to print the first even number from a list
def even(l):
    for i in l:
        if i%2==0:
            return i
        
l=[431,59,43,654,6,]
print(even(l))