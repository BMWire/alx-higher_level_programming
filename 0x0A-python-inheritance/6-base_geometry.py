#!/usr/bin/python3
"""
BaseGeometry module extension
Contains an undefined method area()
"""


class BaseGeometry:
    """A class with public attribute area"""

    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")
