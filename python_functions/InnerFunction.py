# Python program to
# demonstrate accessing of
# variables of nested functions

def f1():
    s = "I love learn python"

    def f2():
        print(s)
    f2()

#Driver's code
f1()