#!/usr/bin/python2

def search_replace(my_list, search, replace):
    # search
    for index, search in enumerate(my_list):
        if search:
            my_list[index] = replace
    return my_list
