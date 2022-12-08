#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    a = list(set_1.difference(set_2))
    b = list(set_2.difference(set_1))
    c = a + b
    return set(c)
