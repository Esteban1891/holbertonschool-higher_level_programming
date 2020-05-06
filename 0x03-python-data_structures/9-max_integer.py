#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        lista = my_list.sort()
    else:
        return (None)
    return(lista[-1])
