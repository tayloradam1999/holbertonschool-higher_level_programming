#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        counter = 0
        for val in range(x):
            if isinstance(my_list[val], int):
                print("{:d}".format(my_list[val]), end="")
                counter += 1
        print()
        return counter
    except TypeError:
        return None
