# Define a dictionary consisting item-cost-quantity for a cafe
# must store the information regarding the items available.
# cost of each item
# quatity of each item
    

items={'Tea':[10,20],'Coffe':[15,20],'Cake':[25,10],'Juice':[20,5],'Chips':[15,25]}
order=[]

print('-----------------------------')
print('|            Menu           |')
print('-----------------------------')
for i,j in items.items():
    print(f"| {i}\t\t-\t {j[0]} |")
print('-----------------------------')

while(True): 
    item=(input("Enter your choice :"))
    quan=(int(input("Enter quantity :")))
    order.append({item:quan})
    yn=input("Order More? y/n :")
    if yn == 'n':
        break
print("Your Order:")
for k in order:
        print(k)