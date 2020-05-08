#!/usr/bin/python3
def best_score(a_dictionary):
    if type(a_dictionary) is dict and len(a_dictionary):
        return max(a_dictionary)
