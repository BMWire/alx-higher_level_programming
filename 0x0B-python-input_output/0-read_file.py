#!/usr/bin/python3

"""
0-read_file module
Contains a function that reads a text file and prints it to stdout
"""


def read_file(filename=""):
    """Read and print text from a file"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end='')
