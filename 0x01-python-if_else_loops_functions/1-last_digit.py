#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number <= 0:
    digit = digit * 1
    if digit == 5:
        val = "greater than 5"
    elif digit == 0:
        val = "0"
    else:
        val = "less than 6 and not 0"
    print("Last digit of {:d} is {:d} and is {:s}".format(number, digit, val))

