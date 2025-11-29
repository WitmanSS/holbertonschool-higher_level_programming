#!/usr/bin/python3
"""
Module for appending text to a UTF-8 file.
"""


def append_write(filename="", text=""):
    """Append text to a UTF-8 file and return number of chars added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
