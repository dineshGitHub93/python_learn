#Any variable created outside a function can be accessed within any function and so they have global scope

x, y = 20,15

def sum():
    sum = x+y
    return sum
def sub():
    sub = x-y
    return sub
def mul():
    mul = x*y
    return mul
def div():
    div = x /y
    return div

print ("\nGlobal variable demo ")
print("Sum of two numbers : ", sum())
print("sub of two numbers : ", sub())
print("Mul of two numbers : ", mul())
print("Div of two numbers : ", div())
#print("Sum of two numbers : ", sum())
