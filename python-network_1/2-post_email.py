#!/usr/bin/python3
"""This is my doc"""


import sys
import urllib.request
import urllib.parse


if __name__ == '__main__':
    url = sys.argv[1]
    mail = sys.argv[2]
    mail = {'email': mail}
    mail = urllib.parse.urlencode(mail).encode()
    req = urllib.request.Request(url, data=mail, method='POST')

    with urllib.request.urlopen(req) as response:
        result = response.read().decode('utf-8')
        print(result)
