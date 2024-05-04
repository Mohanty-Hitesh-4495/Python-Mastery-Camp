#  create a student record with menu  
# 1. add record
# 2. delete record
# 3. view record
# 4. update record

# file=open("friends.txt","w")

fn = "friends.txt"

def add(fn):
    with open(fn,'a') as file:
        name=input("Enter the name of Student :")
        roll=input("Enter the roll no. of Student :")
        cgpa=input("Enter the cgpa of Student :")
        file.write(f"{name}, {roll}, {cgpa}\n")

def show(fn):
    with open(fn,'r') as file:
        content=file.read()
        print(content)

def delete(fn):
    item=input("Enter the student details you want to delete :")
    newcontent = ''
    found=False
    with open(fn,'r') as file:
        for line in file:
            l=line.strip().split(',')
            if item not in line:
                newcontent+=line
            else:
                print("Item found and deleted :)")
                found=True
    if found == True:
        with open(fn,'w') as file:
            file.write(newcontent)

def update(fn):
    item = input("Enter which Student Details you want to update :")
    ask = input("What do you want to be updated :")
    newline = input("Enter the new Value :")

while(True):
    print("***** Main Menu *****")
    print("1. Add Record")
    print("2. Update Record")
    print("3. Delete Record")
    print("4. View Record")
    print("5. Exit")
    opt=int(input("Enter your choice :"))
    if opt == 1:
        print("\nStudent Record Added\n")
        add(fn)
    elif opt == 2:
        print("\nStudent Record Updated\n")
        
    elif opt ==3:
        print("\nStudent Record Deleted\n")
        delete(fn)
    elif opt == 4:
        print("\nDisplayStudent Record\n")
        show(fn)
    elif opt == 5:
        print("Exiting from menu ")
        break
    else:
        print("Please Enter a valid choice :(")
