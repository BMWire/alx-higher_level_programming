#!/usr/bin/python3

"""
Lookup Module.
It defines a function that returns a list of an object's attributes and methods
"""


def lookup(obj):
    """returns a list of available attributes and methods of an object"""
    return dir(obj)
