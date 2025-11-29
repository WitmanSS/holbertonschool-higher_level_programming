#!/usr/bin/python3
"""
Module to write a string to a UTF-8 text file.
"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 file and return numberof characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
