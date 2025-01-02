# Python program to illustrate
# *kwargs for variable number of keyword arguments

def myFun(**kwargs):
    for key , value in kwargs.items():
        print("%s == %s" %(key, value))

#Driver code
myFun(first ='Welcome', mid='To', last='python Learning')