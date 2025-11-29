#!/usr/bin/python3
"""
1-my_list module

Defines the MyList class, which inherits from the built-in list class
and adds a method to print the list in ascending sorted order.
"""


class MyList(list):
    """
    MyList class inherits from list.

    It provides one public instance method: print_sorted.
    """

    def print_sorted(self):
        """
        Prints the list elements in ascending sorted order.
        The original list object is not modified.
        """
        # The built-in sorted() function returns a new sorted list,
        # leaving the original list (self) unchanged.
        print(sorted(self))
