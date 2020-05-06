#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        string = list(my_string)
        for i in string:
            if i in "cC":
                string.remove(i)
        my_string = "".join(string)
    return my_string
