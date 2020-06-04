#!/usr/bin/python3
"""initializate"""


def number_of_lines(filename=""):
    """ that returns the number of lines of a text file"""
    n = 0
    with open(filename, encoding="utf-8") as f:
        line = f.readline()
        n = len(line)
    f.close()
    return n
