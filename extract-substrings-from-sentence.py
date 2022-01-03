"""
Student Name: Aimee Valladares
Purpose: Use the split function to help extract substrings or words from a
         sentence
"""

# Read user input
sentence = input("Enter a sentence: ")

# Split the string into a list of words
listOfWords = sentence.split()

# Display the split function
print("split() Display:", listOfWords)

# Display the number of words using length function
print("There are", len(listOfWords), "words.")

# Initialize variable
sum = 0

# Use for loop to calculate the sum
for word in listOfWords:
    sum += len(word)

# Display the average word length and limit to 2 decimal points
print("The average word length is %0.2f" % (sum / len(listOfWords)))
