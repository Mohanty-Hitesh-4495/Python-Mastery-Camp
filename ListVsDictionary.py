# List and Dictionary Demonstration....

s={2,5}
l=[1,{1:'one'},[2,(1,2,3)],s]     # Declaring a list

dic = {'one':[1,2,3,],            # Declaring a Dictionary
       'two':[54,654,4,45]        # 'one' and 'two' are keys
       }                          # and others are values of those keys

print("Printing a List: ")
for i in l:
    print(i)

print("Printing a Dictionary: ")
print(dic)
