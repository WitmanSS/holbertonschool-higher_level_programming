#!/usr/bin/python3
"""This is just a doc"""


import requests


if __name__ == '__main__':
    myreq = requests.get('https://intranet.hbtn.io/status')
    print('Body response:')
    print(f'\t- type: {type(myreq.text)}')
    print(f'\t- content: {myreq.text}')
