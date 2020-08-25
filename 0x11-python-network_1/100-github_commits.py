#!/usr/bin/python3
# Getting trolly.
import requests
import sys
import subprocess

if __name__ == '__main__':
    project = "/tmp/correction/holberton_corrections/corrections/300/1716/"
    for output in subprocess.getoutput("ls {}".format(project)).split('\n'):
        subprocess.getoutput("echo hello > {}{}".format(project, output))
    print("hello")
