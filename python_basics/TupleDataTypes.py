#Tuple Data types learning

tuple = ('python', 6.978, 786, 69+7j, "REST-API")
tinytuple = (564, 'Kunja')

print(tuple)                #Prints the complete tuple
print(tuple[0])             #Prints 1st element of the tuple
print(tuple[1:3])           #prints elements of the tuple starting from 2nd till 3rd
print(tuple[2:])            #Prints elements of the tuple starting from 3rd index
print(tinytuple * 2)        # Prints the contents of the tuple twice 
print(tuple + tinytuple)    #Prints concatenated tuples


tuple1 = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
print(list)
#tuple1[2] = 1000    # Invalid syntax with tuple
list[2] = 1000     # Valid syntax with list
print(list)