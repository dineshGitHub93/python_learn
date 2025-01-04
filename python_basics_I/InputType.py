#Input() = A function that prompts the user to enter data & returns the entered data as a string.

#input()

name = input("What is your name ? ")
age = int(input("How old are you ? "))
# Input() method return the entered data as a string so we could perform any calculation with numbers
# we have cast this variable to int and then we'll perform operations on top of number

#age +=1 #TypeError: can only concatenate str (not "int") to str
age +=1
print(f"Hello {name} welcome to python learning ")
print(f"You are {age} years old ")


