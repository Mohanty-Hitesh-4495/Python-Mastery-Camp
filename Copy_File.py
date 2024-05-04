# Copy one file to another

with open("friends.txt","r") as file:
    with open("friendscopy.txt","w") as copy:
        copy.write(file.read())

