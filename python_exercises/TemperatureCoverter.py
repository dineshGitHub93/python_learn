#Temperature convert to fahrenheit & celsius by using formual

unit = input("Is the temperature convert into Fahrenheit or celsius (C/F) : ")
temp = float(input("Enter the temperature : "))

if unit == "F":
    temp = round( (9*temp) /5 + 32, 1)
    print(f"The temperature in fahrenheit is : {temp} °F")
elif unit == "C":
    temp = round( (temp-32) * 5 + 9, 1)
    print(f"The temperature in celsius is : {temp} °C")
else:
    print(f"{unit} is an invalid unit of measurement")