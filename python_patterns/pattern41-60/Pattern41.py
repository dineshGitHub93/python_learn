p =1
for x in range(1,5):
    for y in range(1, x+1):
        print("{:2d}".format(p), end=" ")
        p+=1
    print()