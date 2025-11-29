#!/usr/bin/python3
"""this is document"""


class BaseGeometry:
    """this is document"""

    def area(self):
        raise Exception("area() is not implemented")
    """this is document"""

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.name = value
