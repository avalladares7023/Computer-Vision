"""
Student Name: Aimee Valladares
Purpose: Have the Point3D class inherit (extend) the Point 2D class
"""

class Point2D(object):
    """Represents a 2D point"""
    def __init__(self, initX, initY):
        """Create a 2D point at the given initial coordinates"""
        self.x = initX
        self.y = initY

    def move(self, newX, newY):
        """Moves the 2d point to a new location"""
        self.x = newX
        self.y = newY

    def home(self):
        """Moves the 2D point to the origin, i.e., (0, 0)"""
        self.x = 0
        self.y = 0

    def __str__(self):
        """Represents a string representation of the 2D point in the format of (x, y)"""
        return "(" + str(self.x) + "," + str(self.y) + ")"

# The subclass (child class)
class Point3D(Point2D):
    """Represents a 3D point"""

    def __init__(self, initX, initY, initZ):
        """Creates a 3D point at the given initial X, Y, and Z coordinates"""
        Point2D.__init__(self, initX, initY) # Call the constructor in its super class to initialize the X and Y coordinates
        self.z = initZ                       # Initialize the Z coordinate

    def move(self, newX, newY, newZ):
        """Moves the 3D point to a new location"""
        Point2D.move(self, newX, newY)       # Call the move method in its super class
        self.z = newZ                        # Move the Z coordinate

    def home(self):
        """Moves the 3D point to the origin, i.e. (0, 0, 0)"""
        Point2D.home(self)                   # Call the home method in its super class to move the X and Y coordinates
        self.z = 0                           # Move the Z coordinate

    def __str__(self):
        """Returns a string representation of the 3D point in the format of (x, y, z)"""
        return "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"

def main():
    """The main function of this program"""

    # Create a 2D point
    pt1 = Point2D(2, 3)
    # Print the point
    print("Point 1 is at", pt1)
    # Move the point to (6, 8)
    pt1.move(6, 8)
    # Print the point again after moving to new location
    print("Point 1 is now at", pt1)
    # Move the point to the origin
    pt1.home()
    # Print the point again after moving to the origin
    print("Point 1 is now at", pt1)

    # Create a 3D point
    pt2 = Point3D(1, 2, 3)
    # Print the point
    print("Point 2 is at", pt2)
    # Move the point to (5, 6, 5)
    pt2.move(5, 6, 5)
    # Print the point again after moving to new location
    print("Point 2 is now at", pt2)
    # Move the point to the origin
    pt2.home()
    # Print the point again after moving to the origin
    print("Point 2 is now at", pt2)

# Entry point of execution
main()
