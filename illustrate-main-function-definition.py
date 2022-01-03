"""
Student Name: Aimee Valladares
Purpose: Illustrate the definition of a main function.
"""

def main():
    """The main function for this script."""
    # Prompt for a number
    number = float(input("Enter a number: "))

    # Compute and display the square of the number
    print("The square of", number, "is", square(number))

def square(x):
    """Return the square of x."""
    return x * x

# The main entry point for program execution
main()