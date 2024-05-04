# Take user input for the number

n = int(input("Enter the number: "))

if n < 0:
    print("Invalid number :(")
elif n == 0:
    print("0")
elif n == 1:
    print("0 1")
else:
    num1 = 0
    num2 = 1
    # Print the first two Fibonacci numbers
    print(num1, num2, end=" ")
    # Loop to generate Fibonacci sequence
    for i in range(2, n):
        fib = num1 + num2
        print(fib, end=" ")
        num1 = num2
        num2 = fib - num1
