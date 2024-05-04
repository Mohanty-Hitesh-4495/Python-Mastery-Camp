# Can tuple be a value in the dictionary? -> Yes
# Can tuple be a key in the dictionary? -> Yes

dic = {(1,2,3):'one',      # Tuple as Key in dictionary
       (4,5,6):'two'}      # Since Tuple is immutable, we can take it as key
print(dic)

tu=(1,2,3)
dic = {'one':tu,            # Tuple as Value in Dictionary
       'two':(4,5,6)}
print(dic)

tu=(7,8,9)
dic['one'] = tu             # updated the value of key='one'
print(dic)