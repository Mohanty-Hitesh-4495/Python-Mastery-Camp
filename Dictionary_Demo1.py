#  Can a dictionary be a key or value of another dictionary?

# Answer: In Python, dictionary keys must be hashable and immutable.
# Since dictionaries are mutable objects, they cannot be used as keys in another dictionary. 
# However, dictionaries can be used as values in another dictionary.


outer_dict = {                             # Valid: Using a dictionary as a value in another dictionary
    'dict1': {'a': 1, 'b': 2},
    'dict2': {'c': 3, 'd': 4}
}


# outer_dict = {                           # Invalid: Trying to use a dictionary as a key in another dictionary
#     {'a': 1, 'b': 2}: 'value1',          # This will raise a TypeError: unhashable type: 'dict'
#     {'c': 3, 'd': 4}: 'value2'
# }

