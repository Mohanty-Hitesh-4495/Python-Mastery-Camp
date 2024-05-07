# Find the friends from the file from their City Name...

file=open("File Handling/file1.txt","r")
city=input("Enter the city :")

flag=False
for i in file:
    l=i.strip().split(",")
    if city.lower().strip()==l[2].lower().strip():
        print("Name :",l[0])
        print("Number :",l[1])
        flag=True
if flag==False:
    print("Friend is not found in file :(")

# count the number of friends in the file
count=0
for i in file:
    count+=1
print("Friends count = ",count)

