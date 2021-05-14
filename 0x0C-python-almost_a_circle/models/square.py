#!/usr/bin/python3

"""
This module creates a class 'Square'
"""


from models.rectangle import Rectangle


class Square(Rectangle):

    """Square class that inherits from 'Rectangle'"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor method that calls the super class
        This super call will use the logic of the __init__ of
        the 'Rectangle' class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns our attributes values"""
        return '[Square] (%d) %d/%d - %d' % (self.id, self.x,
                                             self.y, self.height)
