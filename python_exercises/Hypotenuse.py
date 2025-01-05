# To find the Hypotenuse of right triangle

import math

a = float(input("Enter value of side A : "))
b = float(input("Enter value of side B : "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f" side c : {round(c, 2)}")