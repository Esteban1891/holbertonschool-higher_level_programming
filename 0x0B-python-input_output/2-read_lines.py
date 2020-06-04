#!/usr/bin/python3
"""initializate"""


def read_lines(filename="", nb_lines=0):
    """ reads n lines of a text file """
    i = len(open(filename).readlines())
    with open(filename, encoding="utf-8") as f:
        if nb_lines <= 0 or nb_lines >= i:
            line = f.read()
            print(line, end="")
        else:
            for _ in range(nb_lines):
                lines = next(f).strip()
                print(lines)
    f.close()
