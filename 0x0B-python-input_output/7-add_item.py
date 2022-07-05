#!/usr/bin/python3

"""
7-add_item module
Contains a function that adds arguments to a list and saves the file
"""

import json
import sys

"""Function imports from 5 and 6 modules"""
save_to_json = __import__('5-save_to_json_file').save_to_json
load_from_json = __import__('6-load_from_json_file').load_from_json

num = len(sys.argv)

try:
    data = load_from_json('add_item.json')
except Exception:
    data = []

# replace the for loop with list extend
listExtend = data.extend(sys.argv[1:])

save_to_json(data, 'add_item.json')
