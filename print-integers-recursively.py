"""
Student Name: Aimee Valladares
Purpose: Print positive integers from 1 to N recursively,
         where N >= 1
"""

def main():
    """The main function of this program"""

    # Prompt for N (the upper bound) for user input
    num = int(input("Please enter a positive integer (i >= 1): "))

    # Print positive integers from 1 to N
    printOnetoN(num)

def printOnetoN(n):
    """Print positive integers from 1 to n recursively"""

    if n == 1:
        print(1, end=" ") # Base case
    else:
        printOnetoN(n-1)  # Recursive case
        print(n, end=" ")

# Entry point of the execution
main()