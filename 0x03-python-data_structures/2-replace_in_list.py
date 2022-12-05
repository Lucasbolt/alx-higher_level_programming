#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    a = len(my_list)
    if idx < 0:
        return my_list
    if idx > (a - 1):
        return my_list
    my_list[idx] = element
    return my_list
