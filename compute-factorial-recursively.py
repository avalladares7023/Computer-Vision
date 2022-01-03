"""
Student Name: Aimee Valladares
Purpose: Compute N! recursively where N >= 0

         N! = 1 * 2 * 3 * ... * (N-1) * N =  N! * N
        (N-1)! = 1 * 2 * 3 * ... * (N-2) * (N-1) = (N-2)! * (N-1)
         2! = 1 * 2 = 1! * 2
         1! = 0! * 1
         0! = 1

         Recursive Definition:
         N! =  Base Case: 1, if n = 0
               Recursive Case: (N-1)! * N, if N > 0
"""

def main():
    """The main function of this program"""

    # Prompt for N (the upper bound) for user input
    num = int(input("Please enter a non-negative integer: "))

    # Compute the sum from 1 to N
    result = factorial(num)

    # Display the result
    print("The factorial of", num , "is", result)

def factorial(n):
    """Compute the factorial of n recursively"""

    if n == 1:
        return 1 # Base case
    else:
        return factorial(n-1) * n # Recursive case

# Entry point of the execution
main()