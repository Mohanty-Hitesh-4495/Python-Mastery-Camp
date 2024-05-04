import random

num = random.randint(1,100)

while(True):
    n = int(input("Guess the number: "))
    if n==num:
        print("Yoooo boii, you have guessed the right number :)")
        break
    elif n<num:
        print("Enter a higher number...")
    else:
        print("Enter a lower number...")
        