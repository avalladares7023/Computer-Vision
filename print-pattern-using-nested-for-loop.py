"""
Student Name: Aimee Valladares
Purpose: Use a nested for loop to display the following pattern in a
         row-major sequence:

         XXXXX
         XXXXX
         XXXXX
         XXXXX
         XXXXX
"""

"""
The following is an example of only using a for loop NOT a nested for loopc

# Start from the 1st row and end at the 5th row
for row in range(1, 6):
    print("XXXXX") # print a row at a time
"""

# Start from the 1st row and end at the 5th row
for row in range(1, 6):
    # Within each, start from the 1st column and end at the 5th column
    for column in range(1, 6):
        print("X", end="") # print a column at a time
        
    print(); # Line feed
