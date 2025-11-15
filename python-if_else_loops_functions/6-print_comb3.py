#!/usr/bin/python3
for i in range(1, 100):
    if int("{:02d}".format(i)) < int("{:02d}".format(i)[::-1]):
        print("{:02d}".format(i), end=', ' if i != 89 else '\n')
