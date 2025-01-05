#Wite a program for calculator using python

operator = input("Enter operator (+,-,*,/,%) : ")
num1 = float(input("Enter value of num1 : "))
num2 = float(input("Enter value of num2 : "))

if(operator == "+"):
    result = num1 + num2
    print(f"Sum of two number : {round(result)}")
elif(operator == "-"):
    result = num1 - num2
    print(f"sub of two number : {round(result)}")
elif(operator == "/"):
    result = num1 / num2
    print(f"div of two number : {round(result, 2)}")
elif(operator == "*"):
    result = num1 * num2
    print(f"Mul of two number : {round(result, 2)}")
elif(operator == "%"):
    result = num1 % num2
    print(f"Mod of two number : {round(result, 2)}")
else:
    print(f"Operator {operator} that you have entered is not valid")