#  given a sentence. sort all the word according to thier length and ignore spaces

sen = input("Enter a sentence :")
ulist = sen.split(" ")
list = []

for i in ulist:
    list.append((len(i),i))
list.sort()

for i in list:
    print(i[1],"->",i[0])



#  given a sentence. sort all the word according to thier length and ignore spaces
 
sen = input("Enter a sentence :")
ulist = sen.split(" ")
dic = {}

for i in ulist:
    dic.update({len(i):i})

list2 = sorted(k for k in dic.keys())

for i in list2:
    print(list[i])