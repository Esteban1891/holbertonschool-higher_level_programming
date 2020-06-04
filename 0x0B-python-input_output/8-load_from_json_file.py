#!/usr/bin/python3
"""initializate"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file""""
    with open(filename, 'r') as h:
        return json.loads(h)

