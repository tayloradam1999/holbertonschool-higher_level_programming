#!/usr/bin/python3
char = 97
for char in range(97, 123):
    if char == 101 or char == 113:
        continue
    print("{}".format(chr(char)), end='')
    char += 1
