#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        a / b
    except ZeroDivisionError:
        division = None
    finally:
        c = "Inside result:"
        print("{} {}".format(c, division))
        return division

