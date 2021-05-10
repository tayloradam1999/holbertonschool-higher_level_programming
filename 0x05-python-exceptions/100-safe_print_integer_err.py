#!/usr/bin/python3


"""
safe_print_integer - Prints an integer with string format
value - Variable that holds any data type
Return: True if value has been correctly printed (value was an int)
"""

import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as x:
        print("Exception: {}".format(x))
        return False
    else:
        return True
