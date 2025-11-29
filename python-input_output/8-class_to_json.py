#!/usr/bin/python3
"""Return a JSON-serializable dict representation of a class instance."""


def class_to_json(obj):
    """Return a dictionary of the instance attributes."""
    return obj.__dict__
