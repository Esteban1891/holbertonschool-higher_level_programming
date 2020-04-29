#!/usr/bin/python3
for letter in range(0, 10):
    for le in range(0, 10):
        if letter >= le:
            continue
        elif letter >= 8 and le >= 9:
            print("{:d}{:d}".format(letter, le))
        else:
            print("{:d}{:d}, ".format(letter, le), end='')
