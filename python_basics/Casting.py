"""
You can specify the data type of a variable with the help of casting
"""
x = int(10)
y = float(10.25)
z = str('25')

print("x = ", x, "and type of x = ", type(x))
print("y = ", y, "and type of y = ", type(y))
print("x = ", x, "and type of z = ", type(z))


#Python variables are case sensitive which means Age and age are two different variables

age = 30
Age = 32

print("age = ", age)
print("Age = ", Age)

#Variables - Multiple Assignment

a=b=c= 10
print(a, " ", b, " ", c)

a,b,c = 15,35,45
print(a, " ", b, " ", c)

# Can assign different types of variables 
a,b,c,d = 11,12.36,"Kunja",True
print(a, " ", b, " ", c, " ", d)
