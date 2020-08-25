#!/usr/bin/python3
"""
Making a request to the GitHub API to display a users id
"""
import requests
from sys import argv


def my_github():

    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(
        'https://api.github.com/user', auth=(username, password))
    data = response.json()
    print(data.get('id'))


if __name__ == "__main__":
    my_github()
