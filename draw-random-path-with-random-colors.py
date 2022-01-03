"""
Student Name: Aimee Valladares
Purpose: Taking a random a walk and leave a trail with random colors
"""

from turtle import *
from random import *

def randomWalk(t, turns = 30): # Set distance = 60
    """Walk randomly"""

    # Randomize the pen color
    t.screen.colormode(255)     # Using the true color system
    
    for count in range(turns):
        # Heading to a random direction
        t.setheading(randint(0, 360))   

        # Randomize the pen color
        t.color(randint(0,255), randint(0,255), randint(0,255))

        # BONUS! Randomize the pen size
        # t.pensize(randint(5, 25))

        # Moving a set distance
        # t.forward(distance)           
        # Moving forward a random distance
        t.forward(randint(60, 100))     

# Entry point of execution
randomWalk(Turtle())


