# Prints all letters except 'e' and 's'
text = "geeksforgeeks"

for i in text:
    if i=='e'or i=='s':
        continue
    print(i)