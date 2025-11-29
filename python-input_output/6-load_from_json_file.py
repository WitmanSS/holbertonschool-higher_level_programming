#!/usr/bin/python3
"""
Module for creating Python objects from JSON files.
"""

import json


def load_from_json_file(filename):
    """Return the Python object represented by a JSON file."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
