#Provide User Input in Python
"""
The input () Function
The raw_input () Function
"""
name = "Kunja"
city = "Hyderabad"

#get input from user at runtime 
#name = input()
#city = input()

#We may give a prompt text
name = input("Enter your name : ")
city = input("Enter your city : ")

print ("Hello My name is", name)
print ("I am from", city)


width = float( input("Enter width : "))
height = float (input("Enter height : "))

area = width*height
print ("Area of rectangle = ", area)