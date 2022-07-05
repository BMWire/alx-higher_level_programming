#!/usr/bin/python3

"""
2-append_write module
Contains a function that appends a string to a file
and returns the length of the text
"""


def append_write(filename="", text=""):
    """Append to a file and print the length of the text"""
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
    return len(text)
