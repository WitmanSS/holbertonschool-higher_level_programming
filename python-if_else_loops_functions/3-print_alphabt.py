#!/usr/bin/python3
for i in range(26):
    if "{:c}".format(97+i) != 'q' and "{:c}".format(97+i) != 'e':
        print("{:c}".format(97+i), end='')
