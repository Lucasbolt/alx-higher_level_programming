#!/usr/bin/python3
"""
Defines a square printing function.
"""

def print_square(size):
    """
    Prints a square of size `size`.

    Arg:
        size (int): length of square.
    
    Raise:
        TypeError: if size is not an integer.
                   if size is float and less than 0.
        ValueError: if size is less than 0.

    """
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    
    for i in range(size):
        print('#' * size)
