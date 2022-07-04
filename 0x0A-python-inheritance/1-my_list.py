#!/usr/bin/python3

"""
MyList module.
It defines a class that inherits from 'list'
"""


class MyList(list):
    """Subclass of list"""

    def __init__(self):
        """Initializes the list"""
        super().__init__()

    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))
