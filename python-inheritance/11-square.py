#!/usr/bin/python3
"""
11-square module: Defines a Square class that inherits from Rectangle.
Includes custom string representation [Square] <width>/<height>.
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
        Returns the default string representation of the Rectangle in the format:
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

    def area(self):
        """
        Calculates and returns the area of the Square.
        """
        # This implementation reuses the area calculation from the parent (Rectangle).
        return super().area()

    def __str__(self):
        """
        Overrides the parent's __str__ method to return the Square description:
        [Square] <width>/<height>
        
        Since Square uses the private attributes defined in the parent (Rectangle),
        we access them via the mangled names internally used by the parent class.
        """
        return f"[Square] {self.__size}/{self.__size}"
        # A more robust approach, assuming __width and __height exist and are set
        # by the parent's __init__ using private naming convention:
        # return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
        # However, using the stored __size is cleaner and safer here.
