# Python if…elif…else Statement

number = int(input("Enter number here :"))

if number > 0:
    print(f"{number} Positive Number")
elif number < 0:
    print(f"{number} Negative Number".format(number))
else:
    print("Zero is nutral number")