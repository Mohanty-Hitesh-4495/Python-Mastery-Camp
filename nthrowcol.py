def get_entity(list,row,col):
    
    if row<0 and row>=len(list):
        return "Invalid row index !"
    
    if col<0 and col>=len(list[row]):
        return "Invalid Column index !"
    
    return list[row][col]

list = [
    [1,5,9,8,10,6,12,56,78,89,48,46],
    [7,4,3,12,23,56,45,78,89,0,60,18],
    [8,2,0,28,39,285,17,58,74,69,2816]
]

r=int(input("Enter the Row index :"))
c=int(input("Enter the Column index :"))

print(get_entity(list,r,c))