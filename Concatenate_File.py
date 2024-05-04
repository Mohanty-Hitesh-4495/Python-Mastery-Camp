# concatanet two files
with open("friends.txt","r") as file:
    c1=file.read()
with open("friendscopy.txt","r") as copy:
    c2=copy.read()
with open("fr.txt","a") as new:
    new.write(f"{c1}\n{c2}")