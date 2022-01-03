"""
Student Name: Aimee Valladares
Purpose: Compute the sum of positive integers from 1 to N recursively,
         where N >= 1
"""

def main():
    """The main function of this program"""

    # Prompt for N (the upper bound) for user input
    num = int(input("Please enter a positive integer (i >= 1): "))

    # Compute the sum from 1 to N
    sum = sumOnetoN(num)

    # Display the sum
    print("The sum from 1 to", num, "is", sum)

def sumOnetoN(n):
    """Compute the sum from 1 to n recursively"""

    if n == 1:
        return 1 # Base case
    else:
        return sumOnetoN(n-1) + n # Recursive case

# Entry point of the execution
main()