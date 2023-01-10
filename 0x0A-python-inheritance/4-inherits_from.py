#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, Dclass):
    """Checks if an object is an inherited instance of a class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), Dclass) and type(obj) != Dclass:
        return True
    return False
