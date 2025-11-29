#!/usr/bin/python3
"""
8-rectangle module

Defines the Rectangle class, now including a static method to compare
two rectangles based on their area.
"""


class Rectangle:
    """
    Defines a rectangle, tracks instance count, and includes a static method
    for comparison.

    Public class attributes:
        number_of_instances (int): Tracks the current number of Rectangle instances.
        print_symbol (any): The symbol used for the string representation.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance and increments the instance count.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        # Increment the instance counter upon successful instantiation
        Rectangle.number_of_instances += 1

        # Note: Using the property setters to perform validation
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        Returns 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using the print_symbol.
        Returns an empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        # Ensure print_symbol is converted to a string before multiplication/joining
        symbol_str = str(self.print_symbol)

        # Create a list of strings, where each string is a row of the symbol
        row = symbol_str * self.__width
        return '\n'.join([row for _ in range(self.__height)])

    def __repr__(self):
        """
        Returns a string representation that can recreate the instance.
        Format: Rectangle(width, height)
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Method called when an instance is about to be deleted.
        Prints a specific message and decrements the instance count.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two Rectangle instances and returns the one with the larger area.

        Args:
            rect_1 (Rectangle): The first rectangle instance.
            rect_2 (Rectangle): The second rectangle instance.

        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
            Rectangle: rect_1 if its area is greater than or equal to rect_2's area,
                       otherwise returns rect_2.
        """
        # Validate that both arguments are instances of Rectangle
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        # Compare areas and return the appropriate instance
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
