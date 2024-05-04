#  can set be consist an list as an element?-> no... 

s={(1,2,3),1,5}
# s={[1,2,3],1,5}           no.. Since list is mutable. it can not be element in a set
# s={{1,2,3},{4,5,6}}       no.. Unhasable
# s={{1:1},'one'}           no.. Unhasable
print(s)
print(len(s))
s.clear()
print(s)
