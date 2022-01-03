"""
Student Name: Aimee Valladares
Purpose: Drawing a polygon by connecting a list of vertices
"""

from turtle import *

def main():
    """The main function of this program"""

    # Create a turtle
    shape = Turtle()

    # Hide the turtle body
    shape.hideturtle()

    # Draw the Polygon
    drawPolygon(shape, [(-30, -20), (-20, 50), (30, 60), (-65, 70)])

def drawPolygon(t, nodes):
    """Connecting a list of nodes to form a polygon"""

    # Before drawing, raise the pen
    t.up()

    # Go to the last node
    t.goto(nodes[-1])

    # Ready to draw, lower the pen
    t.down()
    for (x,y) in nodes:
        t.goto(x,y)

# Entry point of execution
main()