#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return (list(map(lambda new_my_list: new_my_list if new_my_list != search else replace, my_list)))
