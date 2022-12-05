#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    a = []
    for i in my_list:
        a.append(not bool(i % 2))
    return a
