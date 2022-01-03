"""
Student Name: Aimee Valladares
Purpose: Use a while loop to compute the following arithmetic progression:
         53 + 48 + 43 + ... + 3
"""

# Initialize variable
sum = 0      # The accumulator
num = 53     # The first number to be accumulated

# Accumulate the series of numbers
while num >= 3:
    sum = sum + num     # Accumulate a number at a time
    num = num - 5       # Increase the number by 5

# Display the result
print("53 + 48 + 43 + ... + 3 =", sum)
