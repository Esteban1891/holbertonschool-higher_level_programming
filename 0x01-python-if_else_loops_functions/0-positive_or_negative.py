#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    val = "is positive"
elif number == 0:
    val = "is zero"
else:
    val = "is negative"


print("{:d} {:s}".format(number, val))
