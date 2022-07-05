#!/usr/bin/python3

"""
Student_to_JSON module
Contains the definition of a Student class
"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of a student"""
        if attrs is None:
            return self.__dict__

        stud_dict = {}

        for attribute in attrs:
            if hasattr(self, attribute):
                stud_dict[attribute] = getattr(self, attribute)
