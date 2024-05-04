from datetime import datetime


# difference between two dates?
""" currentdate = datetime.now()
d=input("Enter your next Birthday [yyyy-mm-dd]: ")
dateobj=datetime.strptime(d,'%Y-%m-%d')  #convert string date into date object by giving 
print(currentdate)
print(dateobj)
difference = abs (currentdate - dateobj)
print(difference) """


# calculate the age and give next bday of the user...
currentdate = datetime.now()
d=input("Enter your DOB [yyyy-mm-dd]: ")
dateobj=datetime.strptime(d,'%Y-%m-%d')  #convert string date into date object by giving 

if currentdate.month < dateobj.month:
    age = abs(currentdate.year - dateobj.year - 1)
    month = currentdate.month - dateobj.month - 1
else:
    age = abs(currentdate.year - dateobj.year)
    month = currentdate.month - dateobj.month 

if month < 0: # if months comes in negative value then add 12 months 
    month+=12

if currentdate.month > dateobj.month or (currentdate.month == dateobj.month and currentdate.day > dateobj.day):
    nextbday = datetime(currentdate.year+1,dateobj.month,dateobj.day)
else:
    nextbday = datetime(currentdate.year,dateobj.month,dateobj.day)

days = abs (nextbday-currentdate)

print("Age : ",age," years ",month," months")
print("next bday : ",nextbday)
print("next bday in days :",days)

# define a function that takes one year as input and returns next immediate leap year...

