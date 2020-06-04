#!/usr/bin/python3
"""initializate"""
import json


def load_from_json_file(filename):
    """Create object"""
    with open(filename, 'r') as f:
        return json.load(f)
