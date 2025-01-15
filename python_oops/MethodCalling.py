
class Dog:

    def __init__(self,  sound, name):
        self.sound = sound
        self.name = name

    def bark(self):
        print(self.sound)
        
dog1 = Dog("Buddy", 3)
dog1.bark()