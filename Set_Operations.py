# Demostration of Set and its manipulation...

c={'Smarak','Adyasha','Lipsa','Anjani','Susmita','Sonal',"Jadu"}
t={'Prakash','Debasish','Syed','Hitesh','Deba Prakash','Adyasha','Sonal'}

print("t set :",t)
print("c set :",c)

newset={t.pop(),t.pop()}
print("Removed:",newset)

c.discard('Jadu')
t.remove('Deba Prakash')
t.add('Sanjeeb')

print("t set :",t)
print("c set :",c)

t.update(newset)
s=t.union(c)
print("union set :",s)

print("t set:",s.difference(c))
print(s.symmetric_difference(c))

# c.remove('Samir')                      -> keyErorr, since Samir is not exist in set

