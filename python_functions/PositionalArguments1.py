#Positional Arguments

def minus(val1, val2):
    return val1 - val2

a, b = 10, 5
result = a - b
print("Used positional arguments:", result)

# you will get incorrect output because
# expected was (a-b) but you will be getting (b-a)
# because of swapped position of value a and b

a, b = 10, 5
result1 = b - a
print("Used positional arguments:", result1)
