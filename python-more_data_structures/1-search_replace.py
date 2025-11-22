#!/usr/bin/python3

def search_replace(my_list, search, replace):
    lastlist = []
    for i in my_list:
        if i == search:
            lastlist.append(replace)
        else:
            lastlist.append(i)
    return lastlist
