#!/usr/bin/python3
"""initializate"""


def number_of_lines(filename=""):
    """ count lines of file """

    num = 0
    with open(filename, encoding="utf-8") as f:
        line = f.readlines()
        num = len(line)
    f.close()
    return num