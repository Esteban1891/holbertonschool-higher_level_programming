#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        string = list(my_string)
        for a in string:
            if a in "cC":
            string.remove(a)
            my_string = "".join(string)
            return my_string
