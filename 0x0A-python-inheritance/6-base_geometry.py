#!/usr/bin/python3

"""
This module creates an empty class 'BaseGeometry'
Public instance method 'area(self)' that raises an exception with the message
'area() is not implemented'
"""


class BaseGeometry:
    """Empty class"""
    pass

    def area(self):
        """Raises exception"""
        raise Exception("area() is not implemented")
