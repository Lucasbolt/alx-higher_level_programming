#!/usr/bin/python3
"""This module defines a function that appends a text to a file."""


def append_write(filename='', text=''):
    """Appends @text. Create @filename if it doesn't exist."""
    with open(filename, 'a', encoding='utf-8') as fil:
        return fil.write(text)
