#Python Nested if Statements

number = int(input("Enter number here: "))

if number > 0:
    #To Given number is ODD or Even
    if number % 2 ==0:
        print(f"{number} is positive and even number")
    else:
        print(f"{number} is positive but ODD number")
else:
    print(f"{number} is negative number")