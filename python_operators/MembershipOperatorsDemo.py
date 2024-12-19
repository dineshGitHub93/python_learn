#Example of Python Membership Operators

a = 10
b = 20
list = [1,2,3,4,5]

print ("a: {}, b: {}, list: {}".format(a,b,list))

if( a in list):
    print("a is present in the given list")
else:
    print("a is not predent in the given list")

if (b not in list):
    print("B is not present in the given list")
else:
    print("Value of B is present in the given list")

c = b/a

if (c in list):
    print("Value of C: {} is present in the given list".format(c))
else:
    print("Value of C: {} is not present in the given list".format(c))