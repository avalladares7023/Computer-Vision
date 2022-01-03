"""
Student Name: Aimee Valladares
Purpose: Representing a die by a class type
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

def main():
    """The main function of this program"""

    # Creates 2 Dice
    d1 = Die(2)
    d2 = Die()

    # Print the Dice
    print(d1)
    print(d2)

    # Roll both Dice
    d1.roll()
    d2.roll()

    # Print the dice again
    print(d1)
    print(d2)

# Point of execution
main()