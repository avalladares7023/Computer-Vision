"""
Student Name: Aimee Valladares
Purpose: Use a for loop to compute the following arithmetic progression:
         53 + 48 + 43 + ... + 3
"""

# Initialize sum
sum = 0  # The accumulator

# for loop to compute the arithmetic progression
for i in range(53, 3 - 1, -5):
    # sum = sum + i
    sum += i  # Accumulate the number each time

# Print the sum
print("53 + 48 + 43 + ... + 3 =", sum)
