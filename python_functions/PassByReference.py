
# Here x is a new reference to same list lst
def myFun(x):
    x[0] = 22

# Driver Code (Note that lst is modified
# after function call.
list = [9,8,12,46,17,28,20]
print("list before modified ", list)
myFun(list)
print("list is modified afer function call ", list)
