# list can not be member of anything that is mutable   

s={1,"Smarak",["hoi"]}          # such as list cannot be member of set...
print(s)

t={45,3,"sdnfd",{"hitesh"}}     # and set can not be member of set...
print(t)

u={468,{1:"hitu"}}              # same for the dictionary...
print(u)


# Dictionary and its members 

d={[1,2]:"hitesh"}            # list cannot be a key in a dictionary
print(d)                      # Generates Error !!!

d={(1,2):"hitesh"}              # tuple can be a key in dictionary
print(d)                        # Works well :)

d={{4:2}:"hitesh"}              # A dictionary can not be a key in another dictionary
print(d)                        # Generates Error !!!