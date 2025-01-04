#Typecasting = The process of converting a variable from one data type to another data type str(), int(), float(), bool()

name = "Sky"
age = 28
gpa = 7.63
is_student = True

#Convert from int to float
print(f"Variable type before cast({age}) :",type(age))
age = float(age)
print(f"Variable type post cast({age}) :",type(age))
print()

#Convert from float to int
print(f"Variable type before cast({gpa}) :",type(gpa))
gpa = int(gpa)
print(f"Variable type post cast({gpa}) :",type(gpa))
print()

age = 28
#Convert from int to String
print(f"Variable type before cast({age}) :",type(age))
age = str(age)
print(f"Variable type post cast({age}) :",type(age))
print()

#Convert from String to boolean
print(f"Variable type before cast({name}) :",type(name))
name = bool(name)
print(f"Variable type post cast({name}) :",type(name))