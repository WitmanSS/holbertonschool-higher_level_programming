#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    output = []
    for i in my_list:
        if i % 2 == 0:
            output.append(True)
        else:
            output.append(False)
    return output
