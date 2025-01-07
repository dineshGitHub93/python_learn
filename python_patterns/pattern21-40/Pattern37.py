
p =5
for x in range(1,6):
    for y in range(1, x+1):
       print("{:2d}".format(p), end=" ")
    print()
    p = 5-x


for x in range(5,0, -1):
    for y in range(6,x, -1):
        print("{:2d}".format(x), end=" ")
    print()