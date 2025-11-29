#!/usr/bin/python3
"""Define a Student class with JSON-serializable dictionary representation."""


class Student:
    """Student class with first_name, last_name, and age attributes."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of the Student instance."""
        return self.__dict__
