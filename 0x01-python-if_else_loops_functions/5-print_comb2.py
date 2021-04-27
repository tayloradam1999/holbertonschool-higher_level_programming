#!/usr/bin/python3
num = 0
for num in range(0, 100):
    if num == 99:
        print("{}".format(num))
        break
    print("{}, ".format(num), end = '')
    num += 1
