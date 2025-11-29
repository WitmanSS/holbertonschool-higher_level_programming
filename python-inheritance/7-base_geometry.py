#!/usr/bin/python3
"""
7-base_geometry module

Defines the BaseGeometry class with an area method and an
integer validation method.
"""


class BaseGeometry:
    """
    A base class for geometry objects, providing basic methods
    and validation utilities.
    """

    def area(self):
        """
        Calculates the area of the geometry.

        Raises:
            Exception: Always raises an exception with the message
                       "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is an integer greater than 0.

        Args:
            name (str): The name of the value (assumed to be a string).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        # 1. Check if value is an integer
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        # 2. Check if value is greater than 0
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
