#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for a in range(0, x):
        try:
            print(my_list[a], end="")
            counter = counter + 1
        except IndexError:
            break
    print()
    return counter
