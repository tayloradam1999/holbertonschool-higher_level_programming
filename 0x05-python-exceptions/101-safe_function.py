#!/usr/bin/python3

"""
This modules contains a function that
executes a function.
"""


def safe_function(fct, *args):
    """This function executes a function."""
    import sys
    try:
        return fct(*args)
    except Exception as x:
        print("Exception: {}".format(x), file=sys.stderr)
        return None
