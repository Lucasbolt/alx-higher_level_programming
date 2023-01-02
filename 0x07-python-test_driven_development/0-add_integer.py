#!/usr/bin/python3
"""
My addition module.
Takes two `int` or `float` arguments and returns the sum of it.
If arg is float, it will be casted into `int`.
"""

def add_integer(a, b=98):
    """ returns the int sum of a and b """
    if not (isinstance(a, int) or  isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
