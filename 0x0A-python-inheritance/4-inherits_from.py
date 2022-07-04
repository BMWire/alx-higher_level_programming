#!/usr/bin/python3
"""
inherits_from module
Checks if the object is a subclass of the specified class
"""


def inherits_from(obj, a_class):
    """returns true if obj is a subclass of a_class, otherwise false"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
