#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    # return a new dictionary whose values are 2* the value of initial dictionary
    return {key: value * 2 for key, value in a_dictionary.items()}
