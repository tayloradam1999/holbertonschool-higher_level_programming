#!/usr/bin/python3
import json
"""
This module contains a function that returns the JSON
representation of an object (string)
"""


def to_json_string(my_obj):
    """Returns JSON rep. of an object"""
    return json.dumps(my_obj)
