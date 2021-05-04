#!/usr/bin/python3
"""This module writes a class 'Square'.
Initalizes a private instance attribute 'size' with option (self, size=0):.
This module handles TypeErrors and ValueErrors.."""


class Square:
    """Class that initalizes 'size' as a private instance attribute."""
    def __init__(self, size=0):
        """init 'size' for 'Square' Class.
        'Size' must be an int, otherwise raise a TypeError.
        If 'size' is less than 0, raise a ValueError."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be > 0")
        self.__size = size
