#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        my_list.sort()
    else:
        return(None)
    return(my_list[-1])
