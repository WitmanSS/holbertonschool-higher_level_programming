#!/usr/bin/python3
def no_c(my_string):
    returnstr = ""
    for i in my_string:
        if i != "c" and i != "C":
            returnstr += i

    return returnstr
