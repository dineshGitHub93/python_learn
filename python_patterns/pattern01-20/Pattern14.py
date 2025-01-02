
n = 5

for i in range(5,0,-1):
    p = i
    
    for j in range(5,0,-1):
         print("{:2d}".format(p), end=" ")
         p +=5
    print()