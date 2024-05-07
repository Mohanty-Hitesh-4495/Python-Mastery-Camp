import shutil

# File copying
shutil.copy('source_file.txt', 'destination_file.txt')

# File moving
shutil.move('old_location.txt', 'new_location.txt')

# File removal (also works for directories)
shutil.rmtree('directory_to_remove')
