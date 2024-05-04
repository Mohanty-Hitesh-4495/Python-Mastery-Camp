# define a method to print all the unique vowels present in a string
def unique(s):
    l=[]
    vowels=['a','e','i','o','u']
    for i in str.lower(s):
        if i in vowels:
            l.append(i)
    return set(l)

print(unique("Anjani"))