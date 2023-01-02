#!/usr/bin/python3
"""
This module defines a name printing function.
"""

def say_my_name(first_name, last_name=""):
    """
    This functions prints the first and the last name.

    Args:
        first_name (string): first name.
        last_name (string): last name.

    Raises:
        TypeError: if arg entered is not string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
