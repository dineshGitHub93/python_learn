#Python Comparison Operators

a = 10
b = 10

# Check if two variables are equal ro not
if (a ==b ):
    print ("Variable a & b are equal ")
else:
    print ("Variables are not equal")

a, b = 15,20
# Check if two variables are Not equal or equal
if (a !=b ):
    print ("Variables a & b are not equal ")
else :
    print ("Both are equal ")   

# Check if any one variables is lesser than other variable
if ( a < b):
    print("Yes, Variable A is lesser than B")
else :
    print("No, Variable A is not lesser than B ")

# Check if any one variables is greater than other variable
if (a > b):
    print("Yes, Variable A is Greater than B")
else:
    print("No, Variable A is not Greater than B")

#Value Swap
a, b = 12,22
print("Values of a = {}, b = {} before swap".format(a,b))

a,b = b,a
print("Values of a = {}, b = {} afer swap".format(a,b))

if (a <= b):
    print("Varify variable A is lesser or equal than Variable B")
else :
    print("Varify variable A is not lesser or equal than Variable B")

if (a >= b):
    print("Varify variable A is Greater or equal than Variable B")
else :
    print("Varify variable A is not Greater or equal than Variable B")
