#!/usr/bin/python3
"""initialize"""


class MyList(list):
    """create mi class mylist with inheritance"""
    def print_sorted(self):
        """sorted list"""
        print(sorted(self))
