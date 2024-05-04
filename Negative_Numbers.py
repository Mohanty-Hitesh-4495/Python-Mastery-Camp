# define a funtion that returns all negative integers present in a given list


def negative(l):
    return [x for x in l  if isinstance(x,(int,float)) and x<0]

l=[1,5,965,56,-496,-466,4,4565,166,-614,-464,["asdsc",True,-46]]
print(negative(l))
print((lambda x : [i for i in x if i<0])(l))

