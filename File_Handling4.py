# Python program to read a file of friends list
# Search a friend name and print Mobile number...

file=open("file1.txt","r")
name=input("Enter the friends name: ")
flag=False
for i in file:
    l=i.strip().split(",")
    if name.lower()==l[0].lower():
        print("Number :",l[1])
        flag=True
        break
if flag==False:
    print("Friend is not found in file :(")