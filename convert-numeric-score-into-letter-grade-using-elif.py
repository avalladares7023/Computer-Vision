"""
Student Name: Aimee Valladares
Purpose: Converting a numeric score into a letter grade based on the following scale:
         Invalid: above 100
         A: from 90 to 100
         B: from 80 to 89
         C: from 70 to 79
         F: from 0 to 69
         Invalid: below 0
"""

# Enter a numeric score (User Input)
score = int(input("Enter a numeric score (0 - 100): "))

# Convert into a letter grade with multi-way if statement
if score > 100:
    grade = "INVALID"   # above 100
elif score >= 90:
    grade = "A"         # from 90 to 100
elif score >= 80:
    grade = "B"         # from 80 to 89
elif score >= 70:
    grade = "C"         # from 70 to 79
elif score >= 0:
    grade = "F"         # from 0 to 69
else:
    grade = "INVALID"         # below 0


# Display the letter grade
print("The letter grade is", grade)
