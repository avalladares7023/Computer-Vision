"""
Student Name: Aimee Valladares
Purpose: Raise X to the power of N recursively, where X is a floating point
         number and N is an integer greater than or equal to 1 (N >= 1)
"""

def main():
    """The main function of this program"""
    
    # Prompt for the base, the X
    base = float(input("Enter base number which is a floating point number: "))
    # Prompt for the exponent, the N
    exponent = int(input("Enter exponent number which is an integer >= 1: "))

    # Call the recursive function: raise X to Nth power 
    result = pow(base, exponent)

    # Display the result
    print("The result is", result)

def pow(x, n):
    """Raise X to the power of N"""
    if n == 1:
         return x
    else:
         return pow(x, n - 1) * x

# Entry point of execution
main()
