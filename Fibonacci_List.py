# Write a Python program that displays the Fibonacci series up to n terms using a while loop.


def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    count = 0
    while count < n:
        fib_series.append(a)
        a, b = b, a + b
        count += 1
    return fib_series

n = int(input("Enter the number of terms for the Fibonacci series: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    fib_series = fibonacci(n)
print(f"Fibonacci series up to {n} terms:")
print(fib_series)                                   