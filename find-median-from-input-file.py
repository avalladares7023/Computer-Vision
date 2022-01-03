"""
Student Name: Aimee Valladares
Purpose: Find the median for a set of floating-point numbers in an input file.
"""

# Prompt for the input file name
fileName = input("Enter the file name: ")

# Open the input file
inFile = open(fileName, 'r')

# Build a list of numbers by using the numbers in the input file
numbers = []

# Input the text, convert it to numbers, and add the numbers to a list
for line in inFile:
    words = line.split()
    for word in words:
        numbers.append(float(word))

# Sort the list in ascending order
numbers.sort()

# Compute the median
midpoint = len(numbers) // 2
if len(numbers) % 2 == 1:
    median = (numbers[midpoint])
else:
    median = ((numbers[midpoint] + numbers[midpoint - 1]) / 2)

# Print the median
print("The median is", median)
