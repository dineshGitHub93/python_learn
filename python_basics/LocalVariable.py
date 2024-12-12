# Python Local Variables are defined inside a function. We can not access variable outside the function

def sum(x, y):
    sum = x+y
    return sum

print(sum(12,13))

# Function fo multiply
def mul(x, y):
    mul = x*y
    return mul

# Function for Subractions
def sub(x, y):
    sub = x-y
    return sub

# Function for devision
def dev(x, y):
    dev = x/y
    return dev

print("Sum of two numbers : ", sum(15,50))
print("Multiply of two numbers : ", mul(12,10))
print("Subraction of two numbers : ", sub(15,50))
print("division of two numbers : ", dev(15,5))
