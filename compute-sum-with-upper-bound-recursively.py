"""
Student Name: Aimee Valladares
Purpose: Compute the following recursively

         Base Case:
         11, if n = 11

         Recursive Case:
         The sum of N-1 i + N
"""

def main():
    """The main function of this program"""

    # Prompt for N (the upper bound) for user input
    num = int(input("Please enter a positive integer (i >= 11): "))

    # Compute the sum from 11 to N
    sum = sumOnetoN(num)

    # Display the sum
    print("The sum from 11 to", num, "is", sum)

def sumOnetoN(n):
    """Compute the sum from 11 to n recursively"""

    if n == 11:
        return 11 # Base case
    else:
        return sumOnetoN(n-1) + n # Recursive case

# Entry point of the execution
main()
