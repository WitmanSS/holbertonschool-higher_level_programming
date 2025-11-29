#!/usr/bin/python3
"""
6-base_geometry module

Defines the BaseGeometry class with an area method that is not implemented.
"""


class BaseGeometry:
    """
    A base class for geometry objects.
    """

    def area(self):
        """
        Calculates the area of the geometry.

        Raises:
            Exception: Always raises an exception with the message
                       "area() is not implemented", as this method must
                       be defined in derived classes.
        """
        raise Exception("area() is not implemented")
