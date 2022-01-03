"""
Student Name: Aimee Valladares
Purpose: Use a nested for loop to display the following pattern in a
         row-major sequence:
 
         X   X   (1,1)          (1,5)
          X X       (2,2)   (2,4)
           X            (3,3)
          X X       (4,2)   (4,4)
         X   X  (5,1)           (5,5)
"""

# Start from the 1st row and end at the 5th row
for row in range(1, 6):
    # Within each row, start from the 1st column and end at the 5th column
    for column in range(1, 6):
        if ((row == column) or (row + column == 6)):
            print("X", end="")
        else:
            print(" ", end="")
    print() # Line Feed
