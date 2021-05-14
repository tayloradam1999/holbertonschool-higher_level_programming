#!/usr/bin/python3


"""
This module creates a class 'Base'
"""


class Base:
    __nb_objects = 0
    """This class has a constructor and a private class attribute"""
    def __init__(self, id=None):
        """Constructor method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
