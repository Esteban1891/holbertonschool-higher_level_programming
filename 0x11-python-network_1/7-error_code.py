#!/usr/bin/python3
"""initilizate"""
from sys import argv
import requests


def error_code():
    """Script that fetches to url and get X-Request-Id."""
    res = requests.get(argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)


if __name__ == '__main__':
    error_code()
