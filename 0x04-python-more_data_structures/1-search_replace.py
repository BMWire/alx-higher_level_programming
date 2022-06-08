#!/usr/bin/python3

def search_replace(my_list, search, replace):
    def func(element):
        return (element if element != search else replace)
    return list(map(func, my_list))
