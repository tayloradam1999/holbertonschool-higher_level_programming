#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number2 = number % 10
if number < 0:
    number2 = abs(number) % 10
if number2 < 6 and number2 > 0:
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, number2))
elif number2 > 5:
    print("Last digit of {} is {} and is greater than 5"
          .format(number, number2))
else:
    print("Last digit of {} is {} and is 0".format(number, number2))
