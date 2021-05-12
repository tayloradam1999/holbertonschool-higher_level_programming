#!/usr/bin/python3

"""
This module contains a function that writes an object to
a text file using JSON representation
"""


def save_to_json_file(my_obj, filename):
    """Writes an obj to a text file using JSON rep."""
    import json
    with open(filename, mode='w', encoding="UTF-8") as fh:
        jsonString = json.dumps(my_obj)
        fh.write(jsonString)
