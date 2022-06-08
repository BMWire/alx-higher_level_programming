#!/usr/bin/python3

def search_replace(my_list, search, replace):
    for index, search in enumerate(my_list):
        if search:
            my_list[index] = replace
        else: 
            my_list[index] = search
    return my_list
