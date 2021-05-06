#!/usr/bin/python3

"""This module defines a name-printing function
say_my_name - Name printing function
first_name - first string to print
last_name - second string to print
Return - "My name is <first_name> <last_name>."""


def say_my_name(first_name, last_name=""):
    """This defines a function that prints a first and last name.
        Raises a TypeError if:
            Either first_name or last_name are not strings."""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
