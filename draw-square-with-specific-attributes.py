"""
Student Name: Aimee Valladares
Purpose: Draw a red square at a specified location with a specified length for each
         side
"""

from turtle import *

def main():
    """The main function of this program"""
    # Create a turtle
    goofy = Turtle()

    # Hide the turtle
    goofy.hideturtle()

    # Change the pen color
    goofy.pencolor("red")

    # Draw the square
    drawSquare(goofy, 100, 100, 200)

def drawSquare(t, x, y, length):
    """Draw a square at the starting location with the specified length for
       each side"""

    # Before drawing (Raise the pen)
    t.up()

    # Go to the starting location
    t.goto(x, y)

    # Ready to draw (Lower the pen)
    t.down()

    # Draw the square
    for count in range(4):
        t.forward(length)
        t.right(90)

# The entry point of execution
main()