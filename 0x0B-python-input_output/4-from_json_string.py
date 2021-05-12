#!/usr/bin/python3

"""
This module contains a function that returns an object
represented by a JSON string
"""


def from_json_string(my_str):
    """Returns object represented by a JSON string"""
    import json
    return json.loads(my_str)
