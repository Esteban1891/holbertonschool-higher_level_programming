#!/usr/bin/python3
"""initializate"""
import json


def class_to_json(obj):
    """:return"""
    return obj.__dict__
