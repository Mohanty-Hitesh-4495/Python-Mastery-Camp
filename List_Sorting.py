# list sorting in different ways

def mymethod(l):
    return l.startswith('s')

l = ['debasish','hitesh','prakash','jadu','syed','ajay','susmita','satya']

l.sort()                            # sort the same list
n=sorted(l)                         # returns sorted list
l.sort(key=len)                     # sort acording to the length (long-short)
l.sort(key=len,reverse=True)        # sort acording to the length in reverse way (short-long)
# l.sort(mymethod(l))
l1=mymethod(l)
print(l1)

print(n)
print(l)