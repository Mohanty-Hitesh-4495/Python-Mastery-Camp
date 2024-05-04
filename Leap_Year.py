# Python program to take year as user input and display its a leap year or not...

yr = int(input("Enter the year : "))

if yr%4==0:
    print("leap year")
elif yr%100!=0 and yr%400==0:
    print("leap year")
else:
    print("not an leap year")