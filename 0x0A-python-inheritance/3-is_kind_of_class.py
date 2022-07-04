#!/usr/bin/python3
"""
is_kind_of_class module
Checks if the object is an instance of the specified class
"""


def is_kind_of_class(obj, a_class):
    """True if obj is an instance or inherited from a_class, else False"""
    return (isinstance(obj, a_class))
