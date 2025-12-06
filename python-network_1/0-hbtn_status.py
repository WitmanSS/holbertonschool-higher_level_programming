#!/usr/bin/python3
"""This is my doc"""


import urllib.request


url = 'https://intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    data = response.read()
    dt = type(data)
    utfcont = data.decode('utf-8')
    print('Body response:')
    print('\t- type: {}'.format(dt))
    print('\t- content: {}'.format(data))
    print('\t- utf8 content: {}'.format(utfcont))
