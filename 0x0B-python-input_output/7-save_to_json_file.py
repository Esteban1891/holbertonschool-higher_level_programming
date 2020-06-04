#!/usr/bin/python3
"""initializate"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file"""
    with open(filename, 'w') as f:
        file_json = json.dumps(my_obj)
        f.write(file_json)
    f.close()
