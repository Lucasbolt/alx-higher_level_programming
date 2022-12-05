#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    count = len(my_list)
    if idx > (count - 1):
        return my_list
    if idx < 0:
        return my_list
    a = my_list[:]
    a[idx] = element
    return a
