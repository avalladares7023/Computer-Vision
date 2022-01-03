"""
Student Name: Aimee Valladares
Purpose: Computing the Nth element in the Fibonnacci sequence recursively

         Fibonacci sequence:
         0, 1, 1, 2, 3, 5, 8, 13, 21, ...
"""

def main():
    """The main function of this program"""

    # Prompt for fibonnacci number, the Nth element
    element = int(input("Enter Fibonnacci Nth element: "))

    # Call the recursive function: Compute the Nth element of the Fibonacci sequence
    nthElement = fibonacci(element)

    # Display the result
    print("The element is", nthElement)

def fibonacci(n):
    """Compute the Nth element of the Fibonacci sequence"""
    if n <= 2:
        return n - 1    # Base case
    else:
        return fibonacci(n - 2) + fibonacci(n - 1) # Recursive case

# Entry point of execution
main()