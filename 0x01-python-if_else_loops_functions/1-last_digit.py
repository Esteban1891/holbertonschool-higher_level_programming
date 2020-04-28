#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
di = abs(number) % 10

if number <= 0:
    di = di * -1

if di > 5:
    val = "greater than 5"
elif di == 0:
    val = "0"
else:
    val = "less than 6 and not 0"

print("Last digit of {:d} is {:d} and is {:s}".format(number, di, val))
