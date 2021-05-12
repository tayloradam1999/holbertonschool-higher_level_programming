#!/usr/bin/python3

"""
This module contains a function that creates an object
from a JSON file
"""


def load_from_json_file(filename):
    """Creates an obj from a JSON file"""
    import json
    with open(filename) as fh:
        return json.load(fh)
