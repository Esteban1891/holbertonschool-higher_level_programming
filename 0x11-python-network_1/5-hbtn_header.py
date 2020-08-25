#!/usr/bin/python3
"""initializate"""
from sys import argv
import requests


def header():
    """
    Script that fetches to url and get X-Request-Id.
    """
    req = requests.get(argv[1])
    print(req.headers.get('X-Request-Id'))


if __name__ == '__main__':
    header()
