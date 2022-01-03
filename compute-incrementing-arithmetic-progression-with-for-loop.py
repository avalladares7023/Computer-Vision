"""
Student Name: Aimee Valladares
Purpose: Use a for loop to compute the following arithmetic progression:
         3 + 8 + 13 + ... + 53
"""

# Initialize sum
sum = 0  # The accumulator

# for loop to compute the arithmetic progression
for i in range(3, 53 + 1, 5):
    # sum = sum + i
    sum += i  # Accumulate the number each time

# Print the sum
print("3 + 8 + 13 + ... + 53 =", sum)
