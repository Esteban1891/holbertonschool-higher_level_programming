#!/usr/bin/python3
"""
    Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
        Finds a peak in a list of unsorted integers
    """
    # Edge Cases

    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if list_of_integers[1] <= list_of_integers[0]:
        return list_of_integers[0]
    if list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]

    # Main recursion

    mid = len(list_of_integers) // 2
    if list_of_integers[mid] >= list_of_integers[mid - 1] \
            and list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]

    if list_of_integers[mid + 1] > list_of_integers[mid]:
        return(find_peak(list_of_integers[mid + 1:len(list_of_integers)]))

    if list_of_integers[mid - 1] > list_of_integers[mid]:
        return(find_peak(list_of_integers[0:mid]))
