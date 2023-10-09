shopList = ['apple', 'mango', 'game', 'car']

myList = shopList
copiedList = shopList[:]

del myList[0]

print(shopList)
print(myList)
print(copiedList)

print(id(shopList))
print(id(myList))
print(id(copiedList))