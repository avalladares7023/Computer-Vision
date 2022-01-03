"""
Student Name: Aimee Valladares
Purpose: Generate 5 random integers, between 1 and 10, and write them to an output
file called random_integers.txt
"""

# Import all (*) the functions in random
from random import *   # Affects the syntax for calling the function

# Open the output file
outFile = open("random_integers.txt", 'w')

# Generate 5 numbers and write them to random_integers.txt
for count in range(5):
    number = randint(1, 10)  # Generate a number at a time
    outFile.write(str(number) + "\n")

# Close the output file
outFile.close()