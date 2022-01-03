"""
Student Name: Aimee Valladares
Purpose: Draw a C curve fractal to a given level recursively
"""

from turtle import *

def line(t, x1, y1, x2, y2):
    """Draws a line segment between the endpoints"""

    # Prepare to move without drawing
    t.up()
    t.goto(x1, y1)

    # Start drawing
    t.down()
    t.goto(x2, y2)

def cCurve(t, x1, y1, x2, y2, level):
    """Draws a C curve fractal to the given level"""

    if level == 0:
        line(t, x1, y1, x2, y2)                 # Base Case
    else:
        xm = (x1 + x2 + y1 - y2) // 2           # Recursive Case
        ym = (y1 + y2 + x2 - x1) // 2
        cCurve(t, x1, y1, xm, ym, level - 1)
        cCurve(t, xm, ym, x2, y2, level - 1)

def main():
    """The main function of this program"""

    # Prompt the user for the level of the fractal
    level = int(input("Enter a level: "))

    # Create a turtle
    shape = Turtle()

    # Hide the turtle's body
    shape.hideturtle()

    # Draw the C curve fractal
    cCurve(shape, 0, 100, 0, -100, level)

# Main point of execution
main()
