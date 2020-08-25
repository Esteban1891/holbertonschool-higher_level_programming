#!/usr/bin/python3
"""initializate"""
from urllib.request import urlopen
from sys import argv


def hbtn_header_1():
    """sends a request to the URL and
    displays the value of the X-Request-Id"""
    with urlopen(argv[1]) as response:
        print(response.headers.get('X-Request-Id'))


if __name__ == '__main__':
    hbtn_header_1()
