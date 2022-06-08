#!/usr/bin/python3

def uniq_add(my_list=[]):
    # initiate the sum to 0
    summation = 0
    # convert the list to a set - it only has unique
    # values the find the sum of each unique value
    for i in set(my_list):
        summation += i
    return summation
