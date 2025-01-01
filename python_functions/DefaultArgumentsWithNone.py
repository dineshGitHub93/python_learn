# using None as values of the default arguments

print('#List')
def appendItem(itemName, itemList=None):
    if itemList == None:
        itemList = []
    itemList.append(itemName)
    return itemList

#Function call
print(appendItem('Pencel'))
print(appendItem('Note book'))
print(appendItem('Pen'))

# using None as value of default parameter

print('Dictionary')
def addItemToDictionary(itemName, quantity, itemList=None):
    if itemList == None:
        itemList = {}
    itemList[itemName] = quantity
    return itemList

print(addItemToDictionary('Note book', 3))
print(addItemToDictionary('Stick File', 3))
print(addItemToDictionary('sharpner', 8))