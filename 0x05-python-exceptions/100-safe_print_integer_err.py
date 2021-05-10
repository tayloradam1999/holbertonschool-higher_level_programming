#!/usr/bin/python3


"""
safe_print_integer - Prints an integer with string format
value - Variable that holds any data type
Return: True if value has been correctly printed (value was an int)
"""

import sys
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except Exception as x:
        print("Exception: {}".format(x), file=sys.stderr)
        return False
