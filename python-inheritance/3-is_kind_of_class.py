#!/usr/bin/python3
"""
3-is_kind_of_class module

Contains a function that checks if an object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of a_class or a class derived from a_class.

    Args:
        obj (object): The object to check.
        a_class (class): The class or superclass to compare against.

    Returns:
        bool: True if obj is an instance of a_class or its subclass,
              False otherwise.
    """
    return isinstance(obj, a_class)
