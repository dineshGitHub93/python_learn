
k =0
for x in range(1,5):
    k+=x
    for y in range(k, (k-x), -1):
        print(y, end=" ")
    print()