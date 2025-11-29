#!/usr/bin/python3
"""
Module for saving Python objects to JSON files.
"""

import json


def save_to_json_file(my_obj, filename):
    """Write a Python object to a file in JSON format."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
