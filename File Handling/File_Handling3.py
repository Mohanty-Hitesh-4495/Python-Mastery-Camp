# Read the each line of txt file and print it
# Read file1.txt to read freinds details (Name,Number,Address)

file=open("File Handling/file1.txt","r")

for i in file:
    l=i.split(",")
    print("Name: ",l[0])
    print("Number :",l[1])
    print("Address :",l[2])

    