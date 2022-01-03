"""
Student Name: Aimee Valladares
Purpose: Use a while loop to compute the following arithmetic progression:
         3 + 8 + 13 + ... + 53
"""

# Initialize variable
sum = 0     # The accumulator
num = 3     # The first number to be accumulated

# Accumulate the series of numbers
while num <= 53:
    sum = sum + num     # Accumulate a number at a time
    num = num + 5       # Increase the number by 5

# Display the result
print("3 + 8 + 13 + ... + 53 =", sum)
