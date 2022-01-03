"""
Student Name: Aimee Valladares
Purpose: Use a nested while loop to display the following pattern in a
         row-major sequence:

         XXXXX
         XXXXX
         XXXXX
         XXXXX
         XXXXX
"""

# Initialize variables
row = 1     
column = 1  

while row <= 5:  
    while column <= 5:
        print("X", end="") # print a column at a time
        column += 1 # Increment the column

    print(); # Line feed
    column = 1; # Reset for the next row
    row += 1 # Increment the row
