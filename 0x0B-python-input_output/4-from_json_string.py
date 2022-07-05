#!/usr/bin/python3

"""
4-from_json_string module
Contains a function that returns an object represented from a JSON string
"""

import json


def from_json_string(my_str):
    """Return an object from a JSON string"""
    return json.loads(my_str)
