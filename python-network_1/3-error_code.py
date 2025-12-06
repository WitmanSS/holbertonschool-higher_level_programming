#!/usr/bin/python3
"""This is just a doc"""


import urllib.request
import sys
import urllib.error


if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as r:
            print(r.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
