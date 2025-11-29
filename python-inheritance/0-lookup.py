#!/usr/bin/python3
"""
0-lookup module

Contains a function that returns the list of available attributes
and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj (object): The object to inspect.

    Returns:
        list: A list of strings representing the object's attributes and methods.
    """
    return dir(obj)
