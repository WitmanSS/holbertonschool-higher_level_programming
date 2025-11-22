#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = list()
    s = 0
    for i in my_list:
        if i in a:
            pass
        else:
            a.append(i)
            s += i
    return s
