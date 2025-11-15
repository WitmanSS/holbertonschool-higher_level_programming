#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in range(len(str)):
        if ord(str[i]) >= 97:
            result += str[i].swapcase()
        else:
            result += str[i]
    print("{}".format(result))
