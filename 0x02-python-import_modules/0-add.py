#!/usr/bin/python
import sys
a = 1
b = 2
if __name__ == "__main__":
    from add_0 import add

    print("{} + {} = {}".format(a, b, add(a, b)))
