# Take a string as input and count the number of character is present and sort them in ascending order according to thier occurance.


# Take user input
string = input("Enter a String :")

# Convert string to a set to get unique characters
ulist = set(string)
list1 =[]

# Count occurrences of each unique character and store in a list of tuples
for i in ulist:                                             
    list1.append((string.count(i),i))

# Sort the list based on occurrence count
list1.sort()

# Print sorted list
print(list1)

# Print characters and their occurrence counts in descending order
print("Printing All characters and their occurrence:")
for i in range(len(list1)-1,-1,-1):
    print(list1[i][1],"->",list1[i][0])

