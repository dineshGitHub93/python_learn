#Python weight converter

weight = float(input("Enter your weight here : "))
unit = input("Kilograms or pounds ? (K or L) : ")

if unit == "K":
    weight *= 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 2)} {unit}")
elif unit == "L":
    weight /= 2.205
    unit = "Kgs"
    print(f"Your weight is: {round(weight, 2)} {unit}")
else:
    print(f" {unit} is invalid unit ")