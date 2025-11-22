#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        keys = list(a_dictionary.keys())
        values = list(a_dictionary.values())
        biggestvalue = 0
        biggestkey = ""
        for i in range(len(values)):
            if values[i] > biggestvalue:
                biggestvalue = values[i]
                biggestkey = keys[i]
        return biggestkey
    else:
        return None
