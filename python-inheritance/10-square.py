#!/usr/bin/python3
"""
10-square module: Defines a Square class that inherits from Rectangle.
"""


class BaseGeometry:
    """
    A base class for geometry operations, providing validation utilities.
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
        Initializes a new Rectangle instance with validated width and height.
        """
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the Rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of the Rectangle in the format:
        [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    Represents a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The side length of the square. Must be a positive integer.
        """
        # Validate 'size' using the parent's validator
        self.integer_validator("size", size)
        
        # Initialize the Rectangle parent class. For a Square, width and height
        # are both equal to 'size'.
        super().__init__(size, size)
        
        # Store size as a private instance attribute, as required
        self.__size = size

    # Note: The area() method is already correctly implemented in Rectangle (size * size),
    # and the __str__() method returns the format [Rectangle] size/size,
    # so no overriding is strictly necessary for this task, but we include area()
    # for completeness based on the prompt's instruction that area() must be implemented.
    
    def area(self):
        """
        Calculates and returns the area of the Square.
        (This explicitly calls the parent's area, which is size * size).
        """
        return super().area()
