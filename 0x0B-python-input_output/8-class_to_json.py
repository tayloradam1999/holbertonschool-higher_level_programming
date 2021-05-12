#!/usr/bin/python3

"""
This module contains a function that returns the dictionary
description with simple data structure (list, dictionary,
string, integer, and boolean) from JSON serialization of an object
"""


def class_to_json(obj):
    """Returns the dictionary description with simple
    data structure from JSON serialization of an obj"""
    return obj.__dict__
