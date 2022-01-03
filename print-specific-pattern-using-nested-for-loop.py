"""
Student Name: Aimee Valladares
Purpose: Program that uses a nested-for loop to display the following pattern 
         in a row-major sequence:

         OOOOOOX
         OOOOOXX
         OOOOXXX
         OOOXXXX
         OOXXXXX
         OXXXXXX
         XXXXXXX
"""

# Start from the 1st row and end at the 7th row
for row in range(1, 8):
    # Within each row, start from the 1st column and end at the 7th column
    for column in range(1, 8):
        # Conditional statement used to print the pattern
        if ((row + column <= 7)):
            print("O", end="")
        else:
            print("X", end="")
    
    print() # Line Feed