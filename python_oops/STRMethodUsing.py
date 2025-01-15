
class cat:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def __str__(self):
        return f" {self.name} is a {self.gender} cat and {self.age} is year old "
    
cat1 = cat("meera", 2, "Female")
cat2 = cat("penny", 4, "Male")

print(cat1)
print(cat2)