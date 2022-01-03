"""
Student Name: Aimee Valladares
Purpose: Compute the average word length in a sentence.
"""

# Get the variables
sentence = input("Please enter a sentence: ")

# Split the sentence into words
listOfWords = sentence.split()

# Compute the number of words in the sentence
numOfWords = len(listOfWords)

# Initialize the number of characters
numOfChar = 0

# Compute the total number of characters
for word in listOfWords:
    numOfChar += len(word)

# Print the output
print("The average word length is", numOfChar / numOfWords)
