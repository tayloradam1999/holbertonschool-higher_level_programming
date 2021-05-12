#!/usr/bin/python3

"""This module creates a class 'Square' that inherits attributes
from the class 'Rectangle'
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """-Inherits from the 'Rectangle' class
    -size must be private
    -size must be a positive integer, validated by
    'integer_validator'
    -area method must be implemented"""
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns area of our 'Square' object"""
        area = self.__size * self.__size
        return area
