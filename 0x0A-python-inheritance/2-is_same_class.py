#!/usr/bin/python3
"""
is_same_class module
Returns true if the object is the exact class a_class, otherwise false
"""


def is_same_class(obj, a_class):
    """return true if obj is the exact class a_class, otherwise false"""
    return (type(obj) == a_class)
