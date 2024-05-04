# Demonstration of default arguements in method
x=[7]
def values(n=x):
    # l=list(range(n))
    l=len(n)
    print(l)

x=[10,56,4]
print("Length of List passed in method:")
values(x)
print("Length of Default List passed in method:")
values()