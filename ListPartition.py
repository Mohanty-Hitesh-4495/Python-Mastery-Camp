# Given a list one consisting of Numeric(int,float,complex) and Non Numeric values.
# Separate this list into two different list

list=["higuy",654,5.12,"sncj",4+5j,"abx",True,False,[1,2,3,"hofn"]]
l1=[x for x in list if isinstance(x,(int,float,complex)) and not isinstance(x,bool)]
l2=[x for x in list if not isinstance(x,(int,float,complex)) or isinstance(x,bool)]
  
print("Main List: ",list)
print("Numeric List: ",l1)
print("Non-Numeric List: ",l2)