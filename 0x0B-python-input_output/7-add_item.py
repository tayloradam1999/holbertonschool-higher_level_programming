#!/usr/bin/python3

"""
This module contains a function that adds all arguments to a
list, then saves it to a file
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    my_list = load_from_json_file("add_item.json")

except:
    my_list = []

for x in range(1, len(sys.argv)):
    my_list.append(sys.argv[x])

save_to_json_file(my_list, "add_item.json")
