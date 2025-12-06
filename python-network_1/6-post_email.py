#!/usr/bin/python3
"""This is my doc"""


if __name__ == '__main__':
    import sys
    import requests

    respond = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(respond.text)
