#!/usr/bin/python3

"""This module creates a locked class that prevents
the user from dynamically creating new instance attributes,
except if the new instance attribute is called 'first_name'
"""


class LockedClass:
    """Creates the locked class"""
    __slots__ = 'first_name'
