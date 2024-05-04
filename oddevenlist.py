# given a list of integers. make two separate list of odd and even numbers

list = [2,4,1,7,6,8,9,11]
odd = []
even = []
for i in range (len(list)+1):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(f"Odd List: {odd}")
print(f"Even List: {even}")
