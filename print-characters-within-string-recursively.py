"""
Student Name: Aimee Valladares
Purpose: Print the characters within a given nonempty string
"""

def main():
    """The main function of this program"""

    # Prompt for a string
    string = input("Enter a string: ")

    # Print the characters
    print("The characters are:", end = " ")

    # Call the recursive funtion
    printCharacters(string)

def printCharacters(anyString):
    """Print characters in the given string recursively"""

    if len(anyString) == 1:
        print(anyString[0], end = " ")
    else:
        print(anyString[0], end = " ")
        printCharacters(anyString[1:])
