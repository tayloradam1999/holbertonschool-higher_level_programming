#!/usr/bin/python3

"""
This module defines a class 'Rectangle' that
defines a rectangle based on '0-rectangle.py'
"""


class Rectangle:
    """Defines a rectangle with a private instance attribute 'width'
    and 'height'"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter for width that raises Type and Value errors"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter for height that raises Type and Value errors"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
