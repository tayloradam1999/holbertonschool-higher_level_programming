#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = '%s' % str
    if len(str2) > n and n >= 0:
        str2 = str2[0:n:] + str2[n+1::]
    return (str2)
