#!/usr/bin/python3
"""initializate"""
from sys import argv
import requests


def post_email():
    """ URL and an email address, sends a POST request
        to the passed URL with the email as a
        parameter, and finally displays the body of the response.
    """
    data_mail = {'email': argv[2]}
    response = requests.post(argv[1], data=data_mail)
    print(response.text)


if __name__ == '__main__':
    post_email()
