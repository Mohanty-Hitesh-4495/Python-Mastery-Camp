# c is a set of student playing cricket.
# b is a set student playing BADMINTON
# f is a set of student playing football

c={'Satya Sir','Prakash','Anjani','Susmita','Manoj'}
b={'Satya Sir','Susmita','Syed','Gayatri','Lipsa'}
f={'Hitesh','Syed','Satya Sir','Debasish','Prakash'}  

""" rand=c.pop()
print(rand)
c.add(rand)
print(c) """

# find the players that are playing only football or only cricket 
""" u=b.union(c.union(f))
u=u.difference(b)
u=u.difference(c.intersection(f))
print(u) """

# Another approach..


#find the players who is playing both fotball and cricket not badminton
""" cf=c.intersection(f).difference(b)
print(cf) """

# find the players who are playing atleast two games
""" u=c.intersection(b)
n=b.intersection(f)
x=c.intersection(f)
print(n.union(x.union(u)))
 """

# atleast one game
""" u=c.union(f.union(b))
print(u) """

# players playing only 
















































