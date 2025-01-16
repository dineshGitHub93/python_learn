
class Dog:
    #class Variables 
    species = "canine"

    def __init__(self, name, age):
        #Instance variable
        self.name = name
        self.age = age
    
#creates objects 
dog1 = Dog("Johny", 3)
dog2 = Dog("Penny", 2)

# Access class and instance variables
print(dog1.species) #class variables
print(dog1.name) #Instance variables 
print(dog2.name) #instance variables

# Modify instance variables
dog1.name = "Max"
print(dog1.name) #(Updated instance variables)

#Modify class Variables
Dog.species = "Feline"
print(dog1.species) #Updated class variables
print(dog2.species)