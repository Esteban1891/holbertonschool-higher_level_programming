#!/usr/bin/python3
"""
Making a request to the GitHub API to display a users id
"""
import requests
from sys import argv


def my_github():
    """api"""
    username = argv[1]
    password = argv[2]
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(username, password))
    try:
        print(r.json()['id'])
    except KeyError:
        print('None')


if __name__ == "__main__":
    my_github()
