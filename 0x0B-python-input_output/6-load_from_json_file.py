#!/usr/bin/python3

"""
6-load_from_json_file module
Contains a function that creates an Object from a JSON file
"""

import json


def load_from_json_file(filename):
    """Create a JSON file from an object"""

    with open(filename, 'r', encoding="utf-8") as f:
        json.loads(f.read())
