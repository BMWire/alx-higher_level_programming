#!/usr/bin/python3

"""
8-class_to_json module
Contains a function that returns a JSON string representation of a class
"""


def class_to_json(obj):
    """Create a JSON file from an object"""

    return obj.__dict__
