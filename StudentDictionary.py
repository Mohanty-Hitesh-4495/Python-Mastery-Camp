# Make a dictionary of five student having attributes:
# name as values and roll no as key. Now Print the names as per the descending order of roll

student ={36:'hitesh',46:'sanjeeb',67:'syed',9:'Ankit',23:'jadu'}
list = sorted((k for k in student.keys()),reverse=True)
print("Printing Student list Roll number wise (Descending Order):")
for i in list:
    print(i,"->",student[i])

