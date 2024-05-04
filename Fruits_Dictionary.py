# make a dictionarty of fruits where the key is fruitname and value is colour
# make another dictionary where key is flower and value is colour
# make a list of all fruits and flower which are of colour red.

fruit={
    'Apple':'Red',
    'Orange':'Orange',
    'Mango':'Yellow',
    'Banana':'Yellow'
}
flower={
    'Sunflower':'Yellow',
    'Rose':'Red',
    'Lily':'White'
}
print("Fruits:Colour")
print(fruit)
print("Flowers:Colour")
print(flower)

red=[x for x,y in fruit.items() if y=='Red']
red+=[x for x,y in flower.items() if y=='Red']
print(red)