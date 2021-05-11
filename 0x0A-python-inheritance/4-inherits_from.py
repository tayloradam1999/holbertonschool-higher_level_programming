#!/usr/bin/python3

"""
This moodule returns True if the object is an instance of a class that
inherited (directly or indirectly) from a specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """Finds if an object is an instance of an inherited class"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
