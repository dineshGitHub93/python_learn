# Exercise 2 Shopping cart program

#create variables 
item = input("What item would you like to buy ? ")
price = float(input("What is the price ? "))
quantity = int(input("How many would you like to buy "))

total = quantity * price

print(f"You have bought {quantity} x {item}/s ")
print(f"Your total price : {total}")
print("Thank you coming & Visit again")