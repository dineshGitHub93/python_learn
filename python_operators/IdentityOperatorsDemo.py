#Example of Python Identity Operators
a = [1,2,3,4,5]
b = [1,2,3,4,5]

c =a

print(id(a))
print(id(b))
print(id(c))

print(a is c) #True
print(a is b) #False

print(a is not c) #False
print(a is not b) #True

