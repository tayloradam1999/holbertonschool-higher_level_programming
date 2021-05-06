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

    def __str__(self):
        """Prints the rectangle"""
        if self.height == 0 or self.width == 0:
            return ""
        if self.height == 1:
            rectangle = ("#" * self.width) * self.height
        else:
            rectangle = (("#" * self.width) + "\n") * (self.height - 1)\
                + ("#" * self.width)
        return rectangle

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

    def area(self):
        """Public instance method that returns the rectangle's area"""
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """Public instance method that returns the rectangle's perimeter
        If height or width is 0, perimeter is 0"""
        perim = 0
        if self.__width == 0 or self.__height == 0:
            return perim
        else:
            perim = (self.__width * 2) + (self.__height * 2)
            return perim
