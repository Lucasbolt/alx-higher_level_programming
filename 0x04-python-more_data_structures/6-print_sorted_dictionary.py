#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = sorted(list(a_dictionary.keys()))
    for key in a:
        print('{}: {}'.format(key, a_dictionary[key]))
