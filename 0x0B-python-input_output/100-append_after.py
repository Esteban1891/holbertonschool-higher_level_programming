#!/usr/bin/python3
""" append after finding """


def append_after(filename="", search_string="", new_string=""):
    """This function appends text after finding text in a sequence"""
    if not search_string:
        return
    if not new_string:
        return
    with open(filename, 'r') as my_file:
        list_values = my_file.readlines()
    if not list_values:
        return
    i = 0
    variable_len = len(list_values)
    while i != variable_len:
        value = list_values[i].find(search_string)
        if (value != -1):
            list_values.insert(i + 1, new_string)
            i += 1
        i += 1
        variable_len = len(list_values)

    with open(filename, 'w') as my_file:
        my_file.write("".join(list_values))
