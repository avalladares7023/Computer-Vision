"""
Student Name: Aimee Valladares
Purpose: Read in the contents from an input file called in.txt
         and display the contents on the screen. Must use a while loop
         to read, display the file, and check the file's existence.
"""

# Check if the file exists
from os.path import *

if exists("out.txt"):
    # Open the input file in reading mode
    inFile = open("in.txt", 'r')

    # Use a while loop to read in and display a line at a time
    while True: # Forever loop
        line = inFile.readline()    # Read in a line at a time
        if line == "":
            break
        else:
            print(line, end="")
else:
    print("The input file does not exist!")

# No need to close the file because we are not changing contents in the input file.