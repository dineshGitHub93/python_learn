#Example of Python Bitwise Operators

a = 20
b = 10

print('a =', b, ':', bin(a), 'b =', b, ':', bin(b))
c = 0

c = a & b
print("Result of AND is ", c, ':', bin(c))

c = a | b
print("Result of OR is ", c, ':', bin(c))

c = a ^ b
print("Result of EXOR ", c, ':', bin(c))

c = ~a
print("Result of COMPLEMENT ", c, ':', bin(c))

c = a << 2
print("Result of LEFT SHIFT ", c, ':', bin(c))

c = a >> 2
print("Result if RIGHT SHIF", c, ':', bin(c))
