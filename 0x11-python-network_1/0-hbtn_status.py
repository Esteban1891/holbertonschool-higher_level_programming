#!/usr/bin/python3
"""initializate"""
from urllib.request import urlopen


def hbtn_status_0():
    """function show my status"""
    with urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        utf8 = html.decode('utf-8')
        print("Body response:\n\t- type: {}".format(type(html)))
        print("\t- content: {}\n\t- utf8 content: {}".
              format(html, utf8, end=""))


if __name__ == '__main__':
    hbtn_status_0()
