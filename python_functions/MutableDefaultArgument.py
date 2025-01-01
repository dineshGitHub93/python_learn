#mutable default argument values example using python list

# itemName is the name of the item that we want to add to list
# that is being passed, if it is not passed then appending in 
# the default list

def appendItem(itemName, itemList = []):
    itemList.append(itemName)
    return itemList

print(appendItem("Marker"))
print(appendItem("Pencil"))
print(appendItem("Sketch"))

# mutable default argument values example using python dictionary

# itemName is the name of item and quantity is the number of such
# items are there

def addItemToDictionary(itemName, quantity, itemList = {}):
     itemList[itemName] = quantity
     return itemList

print(addItemToDictionary('Notebook', 4))
print(addItemToDictionary('Pencil Box', 6))
print(addItemToDictionary('eraser',4))