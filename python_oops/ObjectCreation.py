
class Dog :
    species = "Canine" #Class attribute 

    def __init__(self, name, age):
        self.name = name #instance attribute
        self.age = age #instance attribute

dog1 = Dog("Johny", 3)

print(dog1.species) # Calling class varibale 
print(dog1.name) # calling instance variable

         