
for x in range(1,6):
    for y in range(1,6):
        p = x+y-1
        if p % 2 == 0:
            print("{:2d}".format(1), end=" ")
        else:
            print("{:2d}".format(0), end=" ")
    print()