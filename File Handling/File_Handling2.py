# Write an examlple progarm to store information regarding your friends

try:
    file=open("File Handling/file1.txt","w")
    while True:
        opt=input("Do you want to add friends info (Yes/No):")
        if opt.lower()=="yes":
            name=input("Enter the name :")
            num=input("Enter the Mobile number :") 
            add=input("Enter the address :")
            file.write(f"{name}, {num}, {add}\n")
        else :
            break
except Exception as e:
    print(e)