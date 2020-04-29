#!/usr/bin/python3


def remove_char_at(str, n):
    string = str

    if len(str) <= n or n < 0:
        return string

    string = string[0: n:] + string[n + 1:]

    return string
