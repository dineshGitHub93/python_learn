
n = 5

for x in range(1, n+1):
    p1 = x
    p2 = n - x + 1

    for y in range(1, n+1):

        if y % 2 == 0:
            print("{:2d}".format(p1), end=" ")
        else:
            print("{:2d}".format(p2), end=" ")
        p1 +=n
        p2 +=n
    
    print()
