#!/usr/bin/python3

"""
1-write_file module
Contains a function that writes to a text file
and returns the length of the input
"""


def write_file(filename="", text=""):
    """Write to a file and print the length of the text"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
    return len(text)
