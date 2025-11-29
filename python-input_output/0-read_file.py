#!/usr/bin/python3
"""
Module to read and print the content of a UTF-8 text file.
"""


def read_file(filename=""):
    """Print the content of a UTF-8 text file."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
