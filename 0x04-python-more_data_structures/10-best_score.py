#!/usr/bin/python3
def best_score(a_dictionary):
    if not bool(a_dictionary):
        return None
    a = list(a_dictionary.values())
    b = max(a)
    for key in a_dictionary.keys():
        if a_dictionary[key] == b:
            return key
