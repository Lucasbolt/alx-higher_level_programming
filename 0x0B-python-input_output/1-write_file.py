#!/usr/bin/python3
"""This module defines a file-writing function."""


def write_file(filename='', text=''):
    """Writes @text to @filename. Creates file if it doesn't exist.
    overwrites existing text in file.
    """
    with open(filename, 'w', encoding='utf-8') as fil:
        return fil.write(text)
