"""
Student Name: Aimee Valladares
Purpose: The Dog class extends (inherits) the Pet class
"""

# The Super Class (Parent Class)
class Pet(object):
    """Represents a pet"""

    def __init__(self, initAge):
        """Constructor that creates a pet with a given age"""
        self.age = initAge

    def getAge(self):
        """Returns the pet's age"""
        return self.age

    def setAge(self, newAge):
        """Resets the pet's age"""
        self.age = newAge

    def __str__(self):
        """Returns the string representation of the pet"""
        return "Age: " + str(self.age)

# The Subclass (Child Class)
class Dog(Pet):
    """Represents a dog"""

    def __init__(self, initAge, initName):
        """Constructor that creates a dog with the given age and name"""
        Pet.__init__(self, initAge)
        self.name = initName

    def getName(self):
        """Returns the dog's name"""
        return self.name

    def setName(self, newName):
        """Resets the dog's name"""
        self.name = newName

    def __str__(self):
        """Returns the string representation of the dog"""
        return Pet.__str__(self) + "\nName: " + self.name

def main():
    """The main function of this program"""

    # Create a pet
    myPet = Pet(3)

    # Print the pet
    print(myPet)

    # Create a dog
    myDog = Dog(2, "Pluto")

    # Print the dog
    print(myDog)

    # Change the dog's age
    myDog.setAge(6)

    # Print the dog again
    print(myDog)
    
# Point of execution
main()