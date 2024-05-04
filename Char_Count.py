# Given a sentence... finding the number of alphabets, digits and special characters present in it.
# Write a Python Program for performing above task...

sen = input("Enter a sentence :")
alpha_count=0                       # Alphabet Counter
num_count=0                         # Numeric Counter
spec_count=0                        # Special Character Counter

for i in sen:
    if i.isalpha():
        alpha_count+=1
    elif i.isdigit():
        num_count+=1
    else:
        spec_count+=1

print("Alphabets: ",alpha_count," \nDigits: ",num_count," \nSpecial Characters: ",spec_count )