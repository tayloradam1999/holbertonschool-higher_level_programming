#!/usr/bin/python3
"""This module creates a class 'Square'.
Initalizes a private instance attribute 'size' with option (self, size=0):.
This module handles TypeErrors and ValueErrors.
Initalizes a public instance method 'def area(self):' that Returns the area."""


class Square:
    """Class that initalizes 'size' as a private instance attribute.
    Initalizes 'area(self)' which returns the area of the current square."""
    def __init__(self, size=0):
        """init 'size' for 'Square' Class.
        'Size' must be an int, otherwise raise a TypeError.
        If 'size' is less than 0, raise a ValueError."""
        if not isinstance(size, int):
                raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be > 0")
        self.__size = size

    def area(self):
        """Public instance method that returns the current square area."""
        area = self.__size ** 2
        return area
