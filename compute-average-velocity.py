"""
Student Name: Aimee Valladares
Purpose: Computing the average velocity of a moving object and
         round the result to 2 decimal places
"""

# Get the variable/constants
time1 = float(input("Enter the initial time (Time 1): "))
location1 = float(input("Enter the initial location (Location 1): "))
time2 = float(input("Enter the final time (Time 2): "))
location2 = float(input("Enter the final location (Location 2):  "))

"""
# Compute the average velocity
averageVelocity = (location2 - location1) / (time2 - time1)

# Round the result to 2 decimal places
averageVelocity = round(averageVelocity, 2)
"""

# Combine the last 2 steps
# Compute the average velocity and round the result to 2 decimal places
averageVelocity = round((location2 - location1) / (time2 - time1), 2)

# Print the output
print("The average velocity of the moving object is", averageVelocity)
