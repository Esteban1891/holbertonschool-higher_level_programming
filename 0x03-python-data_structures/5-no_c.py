#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        string = list(my_string)
        for a in range(string):
            if a in "C" and a in "c":
            string.remove(a)
            my_string = "".join(string)
            return string
