#!/usr/bin/python3

def search_replace(my_list, search, replace):
    for index, search in enumerate(my_list):
        if search:
            my_list[index] = replace
    return my_list
