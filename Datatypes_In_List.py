#  Given a list how many datatypes are present

l = [1,2.5,True,"Hitesh",5+4j]
t=[type(x) for x in l]
s=set(t)

print(f"No. of Datatypes present in  a list = {len(s)}")
print(f"Datatypes are: {s}")    