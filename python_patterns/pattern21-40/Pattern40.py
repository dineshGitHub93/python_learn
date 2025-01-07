

for x in range(5, 0, -1):
    p = 2
    for y in range(6, x, -1):
        print("{:2d}".format(p), end=" ")
        p+=2
    print()

for x in range(1, 6):
    for y in range(1, x+1):
        print((y*2), end=" ")
    print()