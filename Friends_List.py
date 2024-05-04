# make a list for five friends and design a menu for updating

friends = []
opt = 0
while(True):
    print("Main Menu :")
    print("1. Add a Friend.")
    print("2. Remove a Friend.")
    print("3. Display Friends list.")
    print("4. Exit")
    opt=int(input("Enter your choice:"))
    if opt==1:
        name = input("Enter your friend's name:")
        friends.append(name)
    elif opt==2:
        name = input("Enter your friend's name:")
        if name in friends:
            friends.remove(name)
            print(f"{name} was removed successfuly.")
        else:
            print("friend does not exist in list !!!")
    elif opt==3:
        print(friends)
    else:
        print("Exiting from the menu :)")
        break



