"""
Student Name: Aimee Valladares
Purpose: Draw a colurful donut
"""

from turtle import *
from random import *

def main():
    """The main function of this program"""

    # Create a turtle
    donut = Turtle()

    # Hide the turtle's body
    donut.hideturtle()

    # Set the RGB mode
    donut.screen.colormode(255)

    # Start drawing
    for i in range(18):
        # Randomize the pen color
        donut.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))

        # Draw a circle with radius of 20 pixels
        donut.circle(20)

        # Turn 20 degrees to the left
        donut.left(20)

        # Move forward 20 pixels
        donut.forward(20)

# Entry point of execution
main()
