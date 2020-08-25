#!/usr/bin/python3
"""initializate"""
from sys import argv
from urllib.request import urlopen
from urllib.request import Request
import urllib.error


def error_code():
    """script that takes in a URL, sends a request to the URL
       and displays the body of the response (decoded in utf-8).
    """
    url = argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))


if __name__ == '__main__':
    error_code()
