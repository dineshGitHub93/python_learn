#Create a program to demo keyword argument

def student(firstname, lastname):
    print(firstname, lastname)

#Keyword Arguments
print(student(firstname="Blue", lastname="Glass"))
print(student(lastname="Glass", firstname="Blue"))