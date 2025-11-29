#!/usr/bin/python3
"""
2-is_same_class module

Contains a function that checks if an object is exactly an instance
of the specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if obj is exactly an instance of a_class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
