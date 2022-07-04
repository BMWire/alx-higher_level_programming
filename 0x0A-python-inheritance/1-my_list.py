#!/usr/bin/python3

"""
MyList module.
It defines a class that inherits from 'list'
"""


class MyList(list):
    """Initializes the list"""

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """Prints the list in ascending order"""
        return print(sorted(self))
