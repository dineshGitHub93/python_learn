
n = 5

for x in range (1, n+1):
  p1 = x; #1,2,3,4,5 ect...
  p2 = n-x+1; # 5,4,3,2,1 ect...
  for y in range(1, n+1):
     if(y%2==1):
      print("{:2d}".format(p1), end=" ") #1, 
     else:
      print("{:2d}".format(p2), end=" ")
     p1 +=n # 
     p2 +=n #
  print()