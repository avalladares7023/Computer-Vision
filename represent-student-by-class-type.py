"""
Student Name: Aimee Valladares
Purpose: Represent a student by a class type
"""

class Student(object):
    """Represents a student"""

    def __init__(self, initName, initScore):
        """Constructor that creates a student with the given initial values"""
        self.name = initName
        self.score = initScore

    def getName(self):
        """Returns the student's name"""
        return self.name

    def setName(self, newName):
        """Resets the student's Name"""
        self.name = newName
        
    def getScore(self):
        """Returns the student's score"""
        return self.score

    def setScore(self, newScore):
        """Resets the student's Score"""
        self.score = newScore

    def __str__(self):
        """Returns the string representation of the student"""
        return "Name: " + self.name + "\nScore: " + str(self.score)

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