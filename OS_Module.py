# use of the 'os' module in Python 
# 1. file handling,
# 2. detailing functions for file manipulation,
# 3. directory operations,
# 4. path handling.

import os

# File manipulation
os.rename( 'new_file.txt','old_file.txt')
os.remove('file_to_delete.txt')
print(os.path.exists('new_file.txt'))

# Directory operations
os.mkdir('new_directory')
os.rmdir('new_directory')
print(os.listdir())

# Path handling
path = os.path.join('path', 'to', 'file.txt')
absolute_path = os.path.abspath('file.txt')
directory_name = os.path.dirname(absolute_path)
