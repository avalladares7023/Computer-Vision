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

# Convert into a letter grade without multi-way if statement

# Without multi-way if statement (NESTED)
if score > 100:
    grade = "INVALID"   # above 100
else:
    if score >= 90:
        grade = "A"         # from 90 to 100
    else:
        if score >= 80:
            grade = "B"         # from 80 to 89
        else:
            if score >= 70:
                grade = "C"         # from 70 to 79
            else:
                if score >= 0:
                    grade = "F"         # from 0 to 69
                else: 
                    grade = "INVALID"         # below 0

# Display the letter grade
print("The letter grade is", grade)
