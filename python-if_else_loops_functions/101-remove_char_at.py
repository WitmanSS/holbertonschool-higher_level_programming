#!/usr/bin/python3
def remove_char_at(str, n):
    """
    Creates a copy of the string, removing the character at the position n.
    Mimics C array index behavior for position n.
    """
    # 1. Handle invalid index cases (negative or out of bounds)
    if n < 0 or n >= len(str):
        return str

    # 2. Reconstruct the string using slicing
    # Get the part of the string BEFORE index n: str[0:n]
    # Get the part of the string AFTER index n: str[n+1:]
    # Concatenate them to skip the character at index n.
    new_str = str[:n] + str[n + 1:]

    return new_str
