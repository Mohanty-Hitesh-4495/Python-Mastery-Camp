# Given an range find all the prime numbers and print the sum,avg and median of the those prime numbers 

import numpy as np

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))

primes = []

for i in range(start, end + 1):
    if is_prime(i):
        primes.append(i)

prime_sum = np.sum(primes)
prime_avg = np.average(primes)
primes.sort()
prime_median = np.median(primes)
print("Prime numbers within the range:", primes)
print("Sum of all prime numbers:", prime_sum)
print("Average of all prime numbers:", prime_avg)
print("Median of all prime numbers:", prime_median)