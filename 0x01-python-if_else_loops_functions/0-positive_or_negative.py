#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    value =  "is positive"
elif number == 0:
    value = "is zero"
else:
    value = "is negative"
    print("{:d} {:s}".format(number, value))
