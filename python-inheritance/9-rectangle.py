#!/usr/bin/python3
"""
9-rectangle module: Defines a Rectangle class that inherits from BaseGeometry.
This version implements the area method and custom string representation.
"""


class BaseGeometry:
    """
    A base class for geometry operations.
    (Assumed implementation based on project requirements)
    """

    def area(self):
        """
        Raises an Exception indicating that area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Args:
            name (str): The name of the value (e.g., "width").
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Represents a rectangle, inheriting from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle. Must be a positive integer.
            height (int): The height of the rectangle. Must be a positive integer.
        """
        # Validate and set width as a private attribute
        self.integer_validator("width", width)
        self.__width = width

        # Validate and set height as a private attribute
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the Rectangle.
        Overrides the area method from BaseGeometry.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the official string representation of the Rectangle in the format:
        [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
