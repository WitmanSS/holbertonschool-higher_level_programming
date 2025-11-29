#!/usr/bin/python3
"""
7-rectangle module

Defines the Rectangle class, managing instance count and allowing a
customizable symbol for its string representation.
"""


class Rectangle:
    """
    Defines a rectangle, tracks instance count, and uses a customizable
    symbol for printing.

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
