p = 64
for x in range(1,6):
    for y in range(1,6):
        p +=1
        print(chr(p), end=" ")
    print()

print()

n = 5
ch = 0

for x in range(1, n+1):
    for y in range(1, n+1):
        print(chr(ch+65), end=" ")
        if(ch < 26):
            ch +=1
        else:
            ch = 0
    print()