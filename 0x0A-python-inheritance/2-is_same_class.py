#!/usr/bin/python3

"""
This module returns True if the an object is exactly
an instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of a_class,
    otherwise False"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
