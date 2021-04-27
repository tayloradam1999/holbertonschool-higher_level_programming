#!/usr/bin/python3
def fizzbuzz():
    x = 1
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 != 0:
            print("Fizz", end=' ')
        if x % 5 == 0 and x % 3 != 0:
            print("Buzz", end='')
            if x != 100:
                print(" ", end='')
        if x % 5 == 0 and x % 3 == 0:
            print("FizzBuzz", end=' ')
        if x % 5 != 0 and x % 3 != 0:
            print("{}".format(x), end=' ')
