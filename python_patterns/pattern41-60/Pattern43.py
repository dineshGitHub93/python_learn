
for x in range(1,6):
    p = x-1
    for y in range(1,x+1):
        print("{:2d}".format(p+x), end=" ")
        p+=2
    print()