"""
Assignment 2 SOLUTION
Student Name: Aimee Valladares
Purpose: Compute the travelling distance of a bouncing ball
         based on the initial height and how many times the ball
         is allowed to bounce

         EX. 10 + 6 + 6 + 3.6 = 25.6 w/ 2 bounces
             1st Bounce: 10 (dropping) + 6(bouncing)
             2nd Bounce: 6 (dropping) + 3.6(bouncing)
         
"""

# Prompt user for the initial height
initialHeight = float(input("Enter the Initial Ball Height: "))

# Prompt use for how many times the ball is allowed to bounce
times = int(input("Enter the Number of Times the Ball Bounced: "))

# Compute the travelling distance
travellingDistance = 0  # Accumulator
droppingDistance  = initialHeight  # The 1st dropping distance

for time in range(times): # Or range(1, times + 1)
    # The current dropping distance
    bouncingDistance = droppingDistance * 0.6
    
    # Accumulate the travelling distance
    travellingDistance += droppingDistance + bouncingDistance

    # The nex dropping distance
    droppingDistance = bouncingDistance

# Display the travel distance
print("The travelling distance is", travellingDistance)
