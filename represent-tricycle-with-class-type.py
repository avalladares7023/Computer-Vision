"""
Student Name: Aimee Valladares
Purpose: Create a class type to represent a tricycle
"""

class Tricycle(object):
    """Represents a Tricycle"""

    def __init__(self, initSpeed = 0):
        """Creates a tricycle with the given or default initial speed"""
        self.speed = initSpeed

    def getSpeed(self):
        """Returns the tricycle's speed"""
        return self.speed

    def setSpeed(self, newSpeed):
        """Resets the tricycle's speed"""
        self.speed = newSpeed

    def pedal(self):
        """Increases the tricycle's speed by one"""
        self.speed += 1

    def __gt__(self, other):
        """The greater than operator"""
        return self.speed > other.speed

    def __str__(self):
        """Returns a string representation of the tricycle"""
        return "Speed: " + str(self.speed)

def main():
    """The main function of this program"""

    #create two tricycles
    myTricycle = Tricycle(2)
    yourTricycle = Tricycle()

    #print both tricycles
    print("My tricycle has", myTricycle)
    print("Your tricycle has", yourTricycle)

    #change your tricycle's speed to 2
    yourTricycle.setSpeed(2)
 
    #pedal your tricycle
    yourTricycle.pedal()

    #print both tricycles again
    print("My tricycle has", myTricycle)
    print("Your tricycle has", yourTricycle)

    #check if my tricycle is running faster than your tricycle
    if (myTricycle > yourTricycle):
        print("My tricycle is running faster than your tricycle")
    else:
        print("My tricycle is not running faster than your tricycle")

# Entry point of execution
main()
