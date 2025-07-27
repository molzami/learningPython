class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is a {self.__class__.__name__}"
    
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

#-----runnable code -------
rover = Bulldog("Rover", 4)
miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 2)
jack = Dog("Jack", 7)
print(isinstance(rover, Dog))
mbreed = isinstance(miles, Bulldog)
print(mbreed)
print(buddy)
print(jack)