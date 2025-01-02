
#Positional Arguments

def nameAge(name, age):
    print("My name is : ",name,'and my age is : ',age)

# We can get correct output becase argument is given in order
print(nameAge("Dinesh", 31))

#We will get get incorrect output becase argument is not in order 
print(nameAge(27, 'Dinesh'))