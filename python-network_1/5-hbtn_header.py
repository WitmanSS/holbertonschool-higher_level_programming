#!/usr/bin/python3
"""This is my doc"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    respond = requests.get(url)
    print(respond.headers.get('X-Request-Id'))
