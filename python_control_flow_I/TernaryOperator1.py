#conditional Expression = A one-line shortcut for the if-else statement(Ternary Operator)
#                         Print or assign one of two values based on a condition
#                         X if condition else Y

#num = int(input("Please enter number to check ODD or Even : "))

#Print a value using Ternary
#print("Positive" if num > 0 else "Negative")

#Assign a value using Ternary
#result = "Even" if num % 2 == 0 else "ODD"
#print(f"{num} is {result} number")

a = 12
b = 22

#max_num = a if a > b else b
#print(f"Max Number : {max_num}")

#min_num = a if a < b else b
#print(f"Min Number : {min_num}")

age = 15
temperature = 15

#status = "Adult" if age >=18 else "Child"
#whether = "Hot" if temperature >=20 else "COLD"

user_role = "Guest"

access = "Full Access" if user_role == "Admin" else "Limitted Access"

print(access)