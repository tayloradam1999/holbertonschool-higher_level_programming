#!/usr/bin/python3

"""
This module returns the list of available attributes
and methods of an object.
"""


def lookup(obj):
    """Functions that returns list of all available
    methods and attributes of an object"""
    return dir(obj)
