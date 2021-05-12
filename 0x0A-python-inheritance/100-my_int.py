#!/usr/bin/python3

"""
This modules writes a class 'MyInt' that inherits from 'int'
"""


class MyInt(int):
    """-== and != operators are inverted"""
    def __init__(self, integer):
        self.integer = integer

    def __eq__(self, other):
        """Inverts == operator"""
        if self.integer is other:
            return False
        else:
            return not other

    def __ne__(self, other):
        """Inverts != operator"""
        if self.integer < 0:
            if self.integer is not other:
                return True
            else:
                return False
        if self.integer is other:
            return True
        else:
            return False
