#!/usr/bin/python3
"""Module that defines MyList class, inherited from list"""


class MyList(list):
    """Class MyList that inherits from list"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending order)"""
        print(sorted(self))
