# Make a dictionary of 'n' Batsman such that their 'names' are the keys.
# And values (runs,ball,sixes,fours)

bt={}

n=int(input("Enter the number of Batsman:"))
for i in range(n):
    name=input("Enter the name of Batsman:") 
    score=tuple(input("Enter Batsman Details in (Runs,Balls,Sixes,Fours) :").split(","))
    bt[name]={"Runs":int(score[0]),"Balls":int(score[1]),"Sixes":int(score[2]),"Fours":int(score[3])}
    
print(bt)

