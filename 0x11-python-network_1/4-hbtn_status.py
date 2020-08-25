#!/usr/bin/python3
"""initializate"""
import requests


def status():
    """a Python script that fetches https://intranet.hbtn.io/status"""

    data_req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}\n\t- content: {}".
          format(type(data_req.text), data_req.text))


if __name__ == '__main__':
    status()
