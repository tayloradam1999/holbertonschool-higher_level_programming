#!/usr/bin/python3

"""
This module creates an empty class 'BaseGeometry'
Public instance method 'area(self)' that raises an exception with the message
'area() is not implemented'
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry class
    Instantiated with width and height
    width and heigth must be private
    width and height must be positive integers, validated by
    integer_validator in BaseGeometry"""
    def __init__(self, width, height):
        super().__init__()
        if BaseGeometry.integer_validator(self, "width", width):
            self.__width = width
        if BaseGeometry.integer_validator(self, "height", height):
            self.__height = height
