#  arguemnents are two type:

# 1. Variable length of positional arguements OR non-keyword arguementds 
# ----->(stored in tuples)
# ----->(* is used before arguement)

# 2. Variable length of keyword arguements 
# ----->(stored in dictionary)
# ----->(** is used before arguements)


def myfun(**kwargs):
    for k,v in kwargs.items():
        print(v)

myfun(l='one',v='two',s='three')

def vlfun(*args,**kwargs):
    print("\nprinting potional arguements...")
    for i in args:
        print(i,end=" ")
    print("\nprinting Keyword arguements...")
    for k,v in kwargs.items():
        print(v,end=" ")

vlfun(1,2,3,4,5,6,n="hitesh",n1="syed")
vlfun(1,5,6,n="Syed",n1="JAdu",n2="csc",n3="scsc")