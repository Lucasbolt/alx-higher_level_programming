#!/usr/bin/python3
"""
Defines a function that indents line while printing characters.
"""

def text_indentation(text):
    """
    `text_indentation` iterates through characters in ``text``, while printing them.
    If character is any of - `` . , : ? `` it will print 2 lines after each character is encountered.
    
    Args:
        text(string): characters to print.

    Raises:
        TypeError: if `text` isn't string.
    """
    var = ['.', ':', '?']
    ret = []
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    tt = ''
    for i in text:
        if i in var:
            tt += i
            ret.append(tt.lstrip().rstrip())
            ret.append('\n')
            tt = ''
        elif i == '\n':
            ret.append(tt.lstrip().rstrip())
            tt = ''
        else:
            tt += i
    ret.append(tt.lstrip().rstrip())
    c = 0
    for i in ret:
        if i == '\n':
            print(i, end='')
        else:
            if c > 0:
                print('\n', end='')
            print(i, end='')
            c += 1
