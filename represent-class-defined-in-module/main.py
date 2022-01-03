"""
Student Name: Aimee Valladares
Purpose: Represent a student by a class type that is defined in a module
"""

from student import *

# Instantiate a student
myStudent = Student("Albert", 100)

# Print the student
print(myStudent)

# Change the student's name to Tony
myStudent.setName("Tony")

# Change the student's score to 98
myStudent.setScore(98)

#Print the student again
print(myStudent)
