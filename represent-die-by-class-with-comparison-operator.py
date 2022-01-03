"""
Student Name: Aimee Valladares
Purpose: Representing a die by a class type and adding a comparison operators
         and their corresponding methods
"""

from random import randint
class Die(object):
    """Represent a die"""
    def __init__(self, initValue = 1):
        """Creates a die with the given value or default value of 1"""
        self.value = initValue

    def getValue(self):
        """Returns the die's value"""
        return self.value

    def roll(self):
        """Resets the die's value to a random number between 1 and 6"""
        self.value = randint(1, 6)

    def __str__(self):
        """Returns a string representation of a die"""
        return "Value: " + str(self.value)

    def __gt__(self, other):
        """The greater than operator"""
        return self.value > other.value

    def __eq__(self, other):
        """The equality operator"""
        if self is other:
            return True     # The same object
        else:
            if type(self) != type(other):
                return False    # Type mismatch
            else:
                return self.value == other.value # Have the same value or not

def main():
    """The main function of this program"""

    # Creates 2 Dice
    d1 = Die(5)
    d2 = Die()

    # Print the Dice
    print("In d1,", d1)
    print("In d2,", d2)

    # Compare d1 and d2
    if d1 > d2:     # Will be translated into "if d1.__gt__(d2):"
        print("d1 is greater than d2")
    else:
        print("d1 is not greater than d2")

    # Roll both Dice
    d1.roll()
    d2.roll()

    # Print the dice again
    print("In d1,", d1)
    print("In d2,", d2)
    
    # After rolling, compare d1 and d2
    if d1 == d2:
        print("d1 is equal to d2")
    else:
        print("d1 is not equal to d2")

# Point of execution
main()