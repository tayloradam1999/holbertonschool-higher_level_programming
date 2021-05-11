#!/usr/bin/python3

"""
This module returns True if the object is an instance of,
or if the object is an instance of a CLASS that was inherited from
the specified class ; otherwise False"""


def is_kind_of_class(obj, a_class):
    """Finds if instance of class or inherited class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
