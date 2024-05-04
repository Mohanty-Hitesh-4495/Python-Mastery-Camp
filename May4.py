# make dictionary of week-days as keys and your choice colour as values
# Search for all Week days for choice colour
wd={}

weekdays=("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")

for i in weekdays:
    wd[i]=input(f"Enter the Colour for {i}:")

print(wd)

clr=input("Enter the Colour you want to searh:")
l=[]
for k,v in wd.items():
    if v==clr:
        l.append(k)
print(l)

