"""
Student Name: Aimee Valladares
Purpose: Write an object to a file and then read it in from the file
         i.e. Pickling an object
"""

from pickle import *

class Counter(object):
    """Represents a counter"""

    def __init__(self, initValue = 0):
        """"Creates a counter with the default value or a given value"""
        self.value = initValue

    def getValue(self):
        """Return's the counter's value"""
        return self.value
                

    def setValue(self, newValue):
        """Reset the counter's value"""
        self.value = newValue

    def __str__(self):
        """Returns a string representation of a counter"""
        return "Value: " + str(self.value)

def main():
    """The main function of this program"""

    # Create a counter with an initial value of 3
    aCounter = Counter(3)

    # Print the counter
    print(aCounter)

    # Prompt for a file name
    fileName = input("Please enter a file name: ")

    # Open the output file
    outFile = open(fileName, "wb")

    # Write the counter to the output file
    dump(aCounter, outFile)

    # Close the output file
    outFile.close()

    # Open the input file
    inFile = open(fileName, "rb")

    # Read in the counter
    aCounter = load(inFile)

    # Print the counter again
    print(aCounter)
    
# Point of Execution
main()