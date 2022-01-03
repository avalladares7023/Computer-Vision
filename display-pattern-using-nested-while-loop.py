"""
Student Name: Aimee Valladares
Purpose: Use a nested while for loop to display the following pattern in a
         row-major sequence:
 
         X   X   (1,1)          (1,5)
          X X       (2,2)   (2,4)
           X            (3,3)
          X X       (4,2)   (4,4)
         X   X  (5,1)           (5,5)
"""

# Initialize variables
row = 1     # Accumulator
column = 1  # Accumulator

# Start from the 1st row and end at the 5th row
while row <= 5:
    # Within each row, start from the 1st column and end at the 5th column
    while column <= 5:
        if ((row == column) or (row + column == 6)):
            print("X", end="")
        else:
            print(" ", end="")
        column += 1
    print()    # Line Feed
    column = 1 # Reset column value
    row += 1
