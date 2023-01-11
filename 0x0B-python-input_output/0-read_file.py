#!/usr/bin/python3
""" This module defines file-reading (text) function."""


def read_file(filename=""):
    """Prints the contentd of a UTF-8 text file to stdout."""
    with open(filename, encoding='utf-8') as fil:
        print(fil.read(), end='')
