

for x in range(4,-1,-1):
    p1 = x
    for y in range(1,6):
        x +=5
        print(chr(x-5+65), end=" ")
    print() 