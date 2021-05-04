#!/usr/bin/python3


"""
safe_print_integer - Prints an integer with string format
value - Variable that holds any data type
Return: True if value has been correctly printed (value was an int)
"""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except:
        return False
