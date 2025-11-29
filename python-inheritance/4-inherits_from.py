#!/usr/bin/python3
"""
4-inherits_from module

Contains a function that checks if an object is an instance of a class
that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if obj is an instance of a class that inherited from a_class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to check against (the potential superclass).

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
              False otherwise.
    """
    # 1. Check if obj is an instance of a_class or a subclass (using isinstance)
    # AND
    # 2. Check that obj's exact class is NOT a_class (using type)
    return isinstance(obj, a_class) and type(obj) is not a_class
