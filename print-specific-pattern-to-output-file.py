"""
Assignment 4
Student Name: Aimee Valladares
Purpose: Program that uses either a nested for loop to write the following
         pattern in row-major sequence to an output file called out.txt

         OOXOO
         OOXOO
         XXXXX
         OOXOO
         OOXOO
"""

# Open the output file
outFile = open("out.txt", 'w')

# Start from the 1st row and end at the 5th row
for row in range(1, 6):
    # Within each row, start from the 1st column and  end at the 6th column
    for column in range(1, 6):
        # Conditional statement used to print the pattern with each character
        if(row == 3 or column == 3):
            outFile.write("X")  
        else:
            outFile.write("0")
    # New Line for each row
    outFile.write("\n") 

# Close the output file
outFile.close()
