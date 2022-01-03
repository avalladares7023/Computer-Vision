"""
Student Name: Aimee Valladares
Purpose: Read in the contents from an input file called in.txt
         and display the contents on the screen.
"""

# Open the input file in reading mode
inFile = open("in.txt", 'r')

# Read in the entire contents
contents = inFile.read()    # Returns multiple lines into a single string

# Display the contents
print(contents, end = "")

# No need to close the file because we are not changing contents in the input file.
