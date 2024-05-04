# Enter a word and find the number of vowels used in it

word = (input("Enter a word :"))
vowels=['a','e','i','o','u']

count=0
for i in word:
    if i in vowels:
        count+=1

print(count)

vowels = word.count('a')+word.count('e')+word.count('i')+word.count('o')+word.count('u')
print(vowels)