# Can a Set be a key or value in an dictionary? 

# Answer: In Python, a set can be used as a value in a dictionary, but it cannot be used as a key. 
# The reason for this is that keys in a dictionary must be hashable, and sets are mutable objects, which means their contents can change over time. 
# Since mutable objects cannot be hashed, they cannot be used as dictionary keys.


my_dict = {                             # Valid: Using a set as a value in a dictionary
    'key1': {1, 2, 3},
    'key2': {4, 5, 6}
}


# my_dict = {                           # Invalid: Trying to use a set as a key in a dictionary
#     {1, 2, 3}: 'value1',              # This will raise a TypeError: unhashable type: 'set'
#     {4, 5, 6}: 'value2'
# }


#  can none be a key or value in dictionary -> Yes
dic ={None:'one',
      'two':None}
print(dic)

# what will be output?
l=[1,2]
d={1:l}
l.append(5)
l.remove(1)
print(d)            #  the dictionary d has been updated to reflect the changes made to the list l.