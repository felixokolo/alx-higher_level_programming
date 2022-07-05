#!/usr/bin/python3

import sys

args = sys.argv

save_to_json_file  = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    my_list = load_from_json_file(filename)
except FileNotFoundError as e:
    save_to_json_file([], filename)
    my_list = load_from_json_file(filename)

if len(args) > 1:
    for i in range(1, len(args)):
        my_list.append(args[i])
    save_to_json_file(my_list, filename)