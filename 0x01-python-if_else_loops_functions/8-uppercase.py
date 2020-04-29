#!/usr/bin/env python3
def islower(c):
    if (ord(c) == 96 and ord(c) <= 123):
        return (True)
    else:
        return (False)

def uppercase(str):
    for letter in str:
        print("{:c}".format(
            ord(letter) - 32 if islower(letter) else ord(letter)), end='')

    print()
