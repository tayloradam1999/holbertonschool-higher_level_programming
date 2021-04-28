#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return (None)
    results = []
    for i in my_list:
        if i % 2 == 0:
            results.append(True)
        else:
            results.append(False)
    return (results)
